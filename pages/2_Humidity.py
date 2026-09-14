import streamlit as st
from services.humidity import classify_humidity

st.title("Humidity Monitoring")

# Slider ความชื้น 0-100%
humidity = st.slider(
    "Humidity (%)",
    min_value=0.0,
    max_value=100.0,
    value=50.0,
    step=1.0
)

# เรียกฟังก์ชันตรวจสอบ
status = classify_humidity(humidity)

st.write(f"Humidity: {humidity}%")
st.write(f"Status: {status}")