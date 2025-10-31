import matplotlib.pyplot as plt
import pandas as pd
import os

def create_pie_chart(status_summary: pd.DataFrame, output_dir: str) -> str:
    """
    Creates a pie chart of HTTP status codes.
    Returns the saved image file path.
    """
    plt.figure(figsize=(6, 6))
    plt.pie(
        status_summary["count"],
        labels=status_summary["status_code"],
        autopct="%1.1f%%",
        startangle=90
    )
    plt.title("HTTP Status Code Distribution")
    plt.tight_layout()

    output_path = os.path.join(output_dir, "status_pie_chart.png")
    plt.savefig(output_path)
    plt.close()
    return output_path


def create_bar_chart(top_5xx_paths: pd.DataFrame, output_dir: str) -> str:
    """
    Creates a bar chart for top failing 5xx paths.
    Returns the saved image file path.
    """
    if top_5xx_paths.empty:
        return None

    plt.figure(figsize=(8, 5))
    plt.bar(top_5xx_paths["path"], top_5xx_paths["count"], color="salmon")
    plt.title("Top Failing API Paths (5xx)")
    plt.xlabel("Path")
    plt.ylabel("Failure Count")
    plt.xticks(rotation=30, ha='right')
    plt.tight_layout()

    output_path = os.path.join(output_dir, "top_5xx_bar_chart.png")
    plt.savefig(output_path)
    plt.close()
    return output_path


def generate_charts(status_summary: pd.DataFrame, top_5xx_paths: pd.DataFrame, output_dir: str):
    """
    Generates both pie and bar charts, returns their file paths.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    pie_path = create_pie_chart(status_summary, output_dir)
    bar_path = create_bar_chart(top_5xx_paths, output_dir)

    return pie_path, bar_path


if __name__ == "__main__":
    # Demo run
    test_status = pd.DataFrame({
        "status_code": [200, 404, 500, 503],
        "count": [150, 20, 5, 25]
    })
    test_5xx = pd.DataFrame({
        "path": ["/api/a", "/api/b"],
        "count": [4, 2]
    })

    generate_charts(test_status, test_5xx, "data/output")
    print("✅ Charts generated in data/output/")
