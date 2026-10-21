
import requests
import pandas as pd

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 17.385,
    "longitude": 78.487,
    "hourly": "temperature_2m,relative_humidity_2m",
    "forecast_days": 1,
    "timezone": "Asia/Kolkata"
}

response = requests.get(url, params=params, timeout=20)
response.raise_for_status()
data = response.json()

df = pd.DataFrame({
    "Time": data["hourly"]["time"],
    "Temperature_C": data["hourly"]["temperature_2m"],
    "Humidity_Percent": data["hourly"]["relative_humidity_2m"]
})

print("=== First 5 Rows ===")
print(df.head())

print("\n=== Temperature Statistics ===")
print(df["Temperature_C"].describe())

print("\nAverage temperature:",
      round(df["Temperature_C"].mean(), 2), "°C")

print("\nMaximum forecast temperature:",
      df["Temperature_C"].max(), "°C")

print("\nMinimum forecast temperature:",
      df["Temperature_C"].min(), "°C")

df.to_csv("weather_data.csv", index=False)
print("\nSaved data to weather_data.csv")
