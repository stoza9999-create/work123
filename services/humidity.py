def classify_humidity(percent: float) -> str:

    if percent < 0 or percent > 100:
        raise ValueError("Humidity must be between 0 and 100")

    if 40 <= percent <= 60:
        return "NORMAL"

    if 30 <= percent < 40 or 60 < percent <= 70:
        return "WARNING"

    return "CRITICAL"