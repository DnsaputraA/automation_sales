import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression


def detect_trend(
    df: pd.DataFrame,
    date_column: str = "date",
    value_column: str = "sales",
    threshold: float = 0.01
):
    """
    Automatically detect sales trend using Linear Regression.
    """

    # 1. Validasi data
    if df.empty or len(df) < 3:
        return {
            "trend": "Not enough data",
            "slope": 0.0,
            "data_points": len(df)
        }

    # 2. Pastikan urutan waktu benar
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column])
    df = df.sort_values(by=date_column)

    # 3. Siapkan data untuk regression
    X = np.arange(len(df)).reshape(-1, 1)
    y = df[value_column].values.reshape(-1, 1)

    # 4. Train model
    model = LinearRegression()
    model.fit(X, y)

    slope = model.coef_[0][0]

    # 5. Klasifikasi tren
    if slope > threshold:
        trend = "Upward Trend"
    elif slope < -threshold:
        trend = "Downward Trend"
    else:
        trend = "Stable Trend"

    return {
        "trend": trend,
        "slope": round(float(slope), 4),
        "data_points": len(df)
    }
