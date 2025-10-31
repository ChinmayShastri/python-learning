#!/usr/bin/env python3
"""
logstatus.py - parse combined log format, aggregate HTTP status codes,
and optionally generate CSV + PDF reports.
"""

import re
import sys
import csv
import argparse
from collections import Counter
from datetime import datetime
from typing import Optional, Dict, Iterable, List

# ---imports for PDF & charts ---
import matplotlib.pyplot as plt
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
import os

# Regex for common log format
LOG_RE = re.compile(
    r'(?P<host>\S+) \S+ \S+ \[(?P<time>[^\]]+)\] "(?P<method>\S+)? ?(?P<path>[^"]*?) ?(?P<proto>[^"]*?)" (?P<status>\d{3}) (?P<size>\S+) "(?P<referrer>[^"]*)" "(?P<agent>[^"]*)"'
)

TIME_FORMAT = "%d/%b/%Y:%H:%M:%S %z"


# -------------------- CORE LOGIC --------------------

def read_lines(paths: Iterable[str]):
    """Yield lines from files or stdin."""
    for p in paths:
        if p == "-":
            yield from sys.stdin
        else:
            with open(p, "r", encoding="utf-8", errors="replace") as fh:
                yield from fh


def parse_log_line(line: str) -> Optional[Dict]:
    """Return parsed dict or None if invalid."""
    m = LOG_RE.match(line)
    if not m:
        return None
    gd = m.groupdict()
    try:
        ts = datetime.strptime(gd["time"], TIME_FORMAT)
    except Exception:
        ts = None
    return {
        "status": int(gd["status"]),
        "time": ts,
        "path": gd["path"],
        "method": gd["method"],
    }


def aggregate_statuses(parsed_iter: Iterable[Dict]) -> Counter:
    c = Counter()
    for item in parsed_iter:
        if not item:
            continue
        c[item["status"]] += 1
    return c


def write_csv(counter: Counter, out_file):
    total = sum(counter.values())
    with open(out_file, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["status", "count", "percentage"])
        for status, count in sorted(counter.items()):
            pct = (count / total * 100) if total else 0.0
            w.writerow([status, count, f"{pct:.2f}"])


# -------------------- PDF REPORT SECTION --------------------

def generate_pie_chart(counter: Counter, chart_file="chart.png"):
    """Create pie chart image and return filename."""
    labels = [str(k) for k in counter.keys()]
    sizes = list(counter.values())
    plt.figure(figsize=(5, 5))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("HTTP Status Code Distribution")
    plt.tight_layout()
    plt.savefig(chart_file)
    plt.close()
    return chart_file


def get_top_failing_paths(parsed_logs: List[Dict], top_n=5):
    """Find most frequent 5xx paths."""
    path_counter = Counter()
    for rec in parsed_logs:
        if rec and str(rec["status"]).startswith("5"):
            path_counter[rec["path"]] += 1
    return path_counter.most_common(top_n)


def generate_pdf(counter: Counter, top_paths, pdf_file="log_report.pdf"):
    """Generate PDF report with pie chart and summary."""
    chart_file = generate_pie_chart(counter)
    df = pd.DataFrame(list(counter.items()), columns=["Status Code", "Count"])
    df["Percentage"] = (df["Count"] / df["Count"].sum() * 100).round(2)

    doc = SimpleDocTemplate(pdf_file, pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("<b>Web Log Status Report</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    total = sum(counter.values())
    fail_5xx = sum(v for k, v in counter.items() if 500 <= k < 600)
    ok_2xx = sum(v for k, v in counter.items() if 200 <= k < 300)
    summary = (
        f"Total requests: <b>{total}</b><br/>"
        f"2xx Success: <b>{ok_2xx}</b><br/>"
        f"5xx Errors: <b>{fail_5xx}</b><br/>"
        f"Failure Rate: <b>{(fail_5xx / total * 100):.2f}%</b>"
    )
    story.append(Paragraph(summary, styles["Normal"]))
    story.append(Spacer(1, 12))

    story.append(Image(chart_file, width=300, height=300))
    story.append(Spacer(1, 12))

    table_data = [list(df.columns)] + df.values.tolist()
    t = Table(table_data)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold")
    ]))
    story.append(t)
    story.append(Spacer(1, 12))

    if top_paths:
        story.append(Paragraph("<b>Top failing paths (5xx):</b>", styles["Heading2"]))
        for path, count in top_paths:
            story.append(Paragraph(f"{path} → {count} errors", styles["Normal"]))

    doc.build(story)
    print(f"📄 PDF generated: {pdf_file}")


# -------------------- MAIN ENTRY --------------------

def main(argv=None):
    p = argparse.ArgumentParser(description="Aggregate HTTP status codes from logs")
    p.add_argument("--files", nargs="+", required=True, help="Log files or '-' for stdin")
    p.add_argument("--out", default="status_report.csv", help="CSV output file")
    p.add_argument("--prom", action="store_true", help="Print prometheus metrics to stdout")
    p.add_argument("--pdf", action="store_true", help="Generate PDF report with pie chart")
    args = p.parse_args(argv)

    lines = read_lines(args.files)

    # --- Store parsed logs to reuse in PDF later ---
    parsed_logs = [parse_log_line(l) for l in lines]
    counter = aggregate_statuses(parsed_logs)

    # CSV
    write_csv(counter, args.out)
    print(f"✅ CSV written to {args.out}")

    # Prometheus output (optional)
    if args.prom:
        print(format_prometheus(counter))

    # --- NEW: PDF report generation ---
    if args.pdf:
        top_paths = get_top_failing_paths(parsed_logs)
        pdf_name = os.path.splitext(args.out)[0] + ".pdf"
        generate_pdf(counter, top_paths, pdf_name)


def format_prometheus(counter: Counter, metric_name="nginx_status_total"):
    """Prometheus text exposition format."""
    lines = [
        f"# HELP {metric_name} Count of responses by HTTP status code",
        f"# TYPE {metric_name} counter",
    ]
    for status, count in sorted(counter.items()):
        lines.append(f'{metric_name}{{status="{status}"}} {count}')
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    main()
