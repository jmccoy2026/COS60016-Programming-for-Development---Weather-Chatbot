import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")

CITY_ALIASES = {
    "watergate bay": "newquay",
    "the cotswolds": "cheltenham"
}


def get_weather(city):

    # Apply alias mapping
    city = CITY_ALIASES.get(city.lower(), city)

    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url, timeout=5)

        if response.status_code != 200:
            print("API Error:", response.status_code, response.text)  # helpful debug
            return None

        data = response.json()

        forecast = []

        # OpenWeather returns data every 3 hours
        # Take one entry per day
        for i in range(0, 40, 8):

            day_data = data["list"][i]

            forecast.append({
                "date": day_data["dt_txt"],
                "temperature": day_data["main"]["temp"],
                "weather": day_data["weather"][0]["description"],
                "icon": day_data["weather"][0]["icon"]
            })

        return forecast

    except Exception as e:
        print("Weather API error:", e)
        return None


# Test Block
if __name__ == "__main__":

    city = "Watergate Bay"

    weather = get_weather(city)

    print(weather)