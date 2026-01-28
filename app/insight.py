def generate_insight(trend_result: dict) -> str:
    """
    Generate a short textual insight based on trend detection result.
    """

    trend = trend_result.get("trend", "")
    slope = trend_result.get("slope", 0.0)
    points = trend_result.get("data_points", 0)

    if trend == "Upward Trend":
        return (
            f"Sales show an upward trend with consistent growth "
            f"across {points} data points."
        )

    elif trend == "Downward Trend":
        return (
            f"Sales exhibit a downward trend, indicating a decline "
            f"over {points} observed periods."
        )

    elif trend == "Stable Trend":
        return (
            "Sales remain relatively stable with no significant upward "
            "or downward movement detected."
        )

    else:
        return (
            "Insufficient data is available to generate meaningful sales insights."
        )
