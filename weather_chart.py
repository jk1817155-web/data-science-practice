
import requests
import pandas as pd
import matplotlib.pyplot as plt

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 17.385,
    "longitude": 78.487,
    "hourly": "temperature_2m",
    "forecast_days": 1,
    "timezone": "Asia/Kolkata"
}

response = requests.get(url, params=params, timeout=20)
response.raise_for_status()
data = response.json()

df = pd.DataFrame({
    "Time": data["hourly"]["time"],
    "Temperature": data["hourly"]["temperature_2m"]
})

df["Time"] = pd.to_datetime(df["Time"])

plt.figure(figsize=(10, 5))
plt.plot(
    df["Time"],
    df["Temperature"],
    marker="o",
    label="Temperature"
)

plt.title("Hourly Temperature Forecast - Hyderabad")
plt.xlabel("Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("weather_chart.png")
print("Graph saved as weather_chart.png")

plt.show()
