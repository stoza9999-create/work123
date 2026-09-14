def classify_humidity(percent: float) -> str:
    """
    0..100 % -> NORMAL | WARNING | CRITICAL
    นอกช่วง -> ValueError
    """

    # ตรวจสอบค่าที่อยู่นอกช่วง
    if percent < 0 or percent > 100:
        raise ValueError("Humidity must be between 0 and 100")

    # 40-60 = NORMAL
    if 40 <= percent <= 60:
        return "NORMAL"

    # น้อยกว่า 30 หรือมากกว่า 70 = CRITICAL
    if percent < 30 or percent > 70:
        return "CRITICAL"

    # 30-40 และ 60-70 = WARNING
    return "WARNING"