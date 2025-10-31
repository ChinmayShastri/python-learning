import sys, os
from modules.log_parser import load_log_data
from modules.analysis import generate_analysis
from modules.charts import generate_charts
from modules.report_generator import generate_pdf_report

OUTPUT_DIR = "data/output"

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_logfile>")
        sys.exit(1)

    log_file = sys.argv[1]
    df = load_log_data(log_file)

    status_summary, top_5xx_paths = generate_analysis(df)
    pie_path, bar_path = generate_charts(status_summary, top_5xx_paths, OUTPUT_DIR)

    output_pdf = os.path.join(OUTPUT_DIR, "log_report.pdf")
    generate_pdf_report(status_summary, top_5xx_paths, pie_path, bar_path, output_pdf)
