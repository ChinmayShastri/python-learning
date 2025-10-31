import pandas as pd

def summarize_status_codes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a summary of how many times each status code occurred
    and its percentage share.
    """
    summary = df["status_code"].value_counts().reset_index()
    summary.columns = ["status_code", "count"]
    total = summary["count"].sum()
    summary["percentage"] = (summary["count"] / total * 100).round(2)
    return summary.sort_values(by="status_code")


def get_top_failing_paths(df: pd.DataFrame, limit: int = 5) -> pd.DataFrame:
    """
    Filters 5xx errors and finds which paths failed most often.
    Returns top N paths.
    """
    df_5xx = df[df["status_code"].between(500, 599)]
    if df_5xx.empty:
        return pd.DataFrame(columns=["path", "count"])
    
    top_fails = (
        df_5xx["path"]
        .value_counts()
        .reset_index()
        )
    top_fails.columns = ["path", "count"]
    top_fails = top_fails.head(limit)

    return top_fails


def generate_analysis(df: pd.DataFrame):
    """
    Main analysis entry point — combines all insights.
    Returns:
      - status_summary: DataFrame of code counts
      - top_5xx_paths: DataFrame of top failing endpoints
    """
    status_summary = summarize_status_codes(df)
    top_5xx_paths = get_top_failing_paths(df)

    return status_summary, top_5xx_paths


if __name__ == "__main__":
    # For standalone testing (optional)
    data = {
        "path": ["/api/v1/a", "/api/v1/b", "/api/v1/a", "/api/v1/b", "/api/v1/a"],
        "status_code": [200, 503, 503, 200, 500],
    }
    df = pd.DataFrame(data)
    summary, top_fails = generate_analysis(df)
    print("\nStatus Summary:\n", summary)
    print("\nTop 5xx Paths:\n", top_fails)
