import csv
import os
from datetime import datetime


LOG_DIR = "outputs/logs"
LOG_FILE = "analysis_log.csv"


def log_analysis(trend_result: dict, insight: str):
    """
    Log analysis result into a CSV file.
    """

    # Pastikan folder logs ada
    os.makedirs(LOG_DIR, exist_ok=True)

    log_path = os.path.join(LOG_DIR, LOG_FILE)

    file_exists = os.path.isfile(log_path)

    with open(log_path, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Tulis header kalau file baru
        if not file_exists:
            writer.writerow([
                "timestamp",
                "trend",
                "slope",
                "data_points",
                "insight"
            ])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            trend_result.get("trend"),
            trend_result.get("slope"),
            trend_result.get("data_points"),
            insight
        ])
