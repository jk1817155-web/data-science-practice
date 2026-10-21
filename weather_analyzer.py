
import requests

# Example coordinates: Hyderabad
url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 17.385,
    "longitude": 78.487,
    "current": "temperature_2m,relative_humidity_2m,wind_speed_10m"
}

try:
    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()
    data = response.json()

    weather = data["current"]

    print("=== Weather Data Analyzer ===")
    print("Temperature:", weather["temperature_2m"], "°C")
    print("Humidity:", weather["relative_humidity_2m"], "%")
    print("Wind speed:", weather["wind_speed_10m"], "km/h")
    print("Time:", weather["time"])

except (requests.exceptions.RequestException, KeyError) as error:
    print("Could not retrieve weather data:", error)
