import requests
import json
from datetime import datetime

CITY_NAME = "London"
COUNTRY_CODE = "GB"
API_KEY = "e9aa44fd98547d5c4f0bde33865845be"  # open weather key

# === 1. Get city coordinates ===
geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={CITY_NAME},{COUNTRY_CODE}&limit=1&appid={API_KEY}"
geo_response = requests.get(geo_url).json()

if not geo_response:
    print("City not found!")
    exit()

lat, lon = geo_response[0]['lat'], geo_response[0]['lon']
print(f"Found coordinates: {lat}, {lon}")

# === 2. Fetch current weather ===
weather_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
weather_response = requests.get(weather_url).json()

# Save to a file with timestamp
timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
filename = f"data/weather_{timestamp}.json"

with open(filename, "w") as f:
    json.dump(weather_response, f, indent=2)

print(f"Weather data saved to {filename}")
