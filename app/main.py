import pandas as pd

from analysis import detect_trend
from insight import generate_insight
from visualization import generate_sales_chart
from logger import log_analysis


def run_automation(csv_path: str):
    """
    Run full AI automation pipeline on sales data.
    """

    # 1. Load data
    df = pd.read_csv(csv_path)

    # 2. Detect trend (AI)
    trend_result = detect_trend(df)

    # 3. Generate insight
    insight = generate_insight(trend_result)

    # 4. Generate visualization
    chart_path = generate_sales_chart(df, trend_result)

    # 5. Log result
    log_analysis(trend_result, insight)

    return {
        "trend_result": trend_result,
        "insight": insight,
        "chart_path": chart_path
    }


if __name__ == "__main__":
    result = run_automation("data/sales_data.csv")

    print("=== AI AUTOMATION RESULT ===")
    print("Trend:", result["trend_result"]["trend"])
    print("Insight:", result["insight"])
    print("Chart saved at:", result["chart_path"])
