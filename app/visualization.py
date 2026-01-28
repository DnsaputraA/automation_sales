import os
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd


CHART_DIR = "outputs/charts"


def generate_sales_chart(
    df: pd.DataFrame,
    trend_result: dict,
    date_column: str = "date",
    value_column: str = "sales"
):
    """
    Automatically generate and save sales trend visualization.
    """

    # Pastikan folder output ada
    os.makedirs(CHART_DIR, exist_ok=True)

    # Urutkan data berdasarkan tanggal
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(by=date_column)

    # Buat nama file unik
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"sales_trend_{timestamp}.png"
    filepath = os.path.join(CHART_DIR, filename)

    # Buat plot
    plt.figure()
    plt.plot(df[date_column], df[value_column])
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.title(f"Sales Trend — {trend_result.get('trend')}")
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Simpan chart
    plt.savefig(filepath)
    plt.close()

    return filepath
