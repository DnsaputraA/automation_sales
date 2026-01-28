import pandas as pd
from app.analysis import detect_trend
from app.insight import generate_insight
from app.visualization import generate_sales_chart

df = pd.read_csv("data/sales_data.csv")

trend_result = detect_trend(df)
insight = generate_insight(trend_result)

chart_path = generate_sales_chart(df, trend_result)

print("Chart saved at:", chart_path)
