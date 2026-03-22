from cache import get_cached_weather, save_to_cache
from weather_api import get_weather
from datetime import datetime
import sqlite3


# Supported locations
LOCATIONS = [
    "cumbria",
    "corfe castle",
    "the cotswolds",
    "cambridge",
    "bristol",
    "oxford",
    "norwich",
    "stonehenge",
    "watergate bay",
    "birmingham"
]


# Conversation state
last_location = None
awaiting_followup = False


# Get attraction from SQLite database
def get_attraction(city):

    conn = sqlite3.connect("attractions.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT name, maps FROM attractions WHERE city=?",
        (city,)
    )

    result = cursor.fetchone()
    conn.close()

    if result:
        return {
            "name": result[0],
            "maps": result[1]
        }

    return None


# Extract location from user input
def extract_location(user_input):

    text = user_input.lower()

    for location in LOCATIONS:
        if location in text:
            return location

    return None


# Suggest activity based on weather
def suggest_activity(weather):

    weather = weather.lower()

    if "rain" in weather:
        return "It may be a good day to visit museums or indoor attractions."

    if "clear" in weather or "sun" in weather:
        return "Great weather for sightseeing and outdoor walking tours."

    if "cloud" in weather:
        return "A good day to explore local landmarks."

    return "Check local attractions during your visit."


# Weather rating
def get_weather_rating(temp):

    if temp >= 22:
        return "Excellent ☀️"
    elif temp >= 16:
        return "Good 🌤️"
    elif temp >= 10:
        return "Okay ☁️"
    else:
        return "Cold ❄️"


# Best destination logic
def get_best_destination():

    best_city = None
    best_temp = -999

    for city in LOCATIONS:

        weather_data = get_cached_weather(city)

        if weather_data is None:
            weather_data = get_weather(city)

            if weather_data:
                save_to_cache(city, weather_data)

        if weather_data:

            avg_temp = sum(day["temperature"] for day in weather_data) / len(weather_data)

            if avg_temp > best_temp:
                best_temp = avg_temp
                best_city = city

    return best_city, round(best_temp, 1)


# Smart follow-up
def generate_smart_followup(current_city, best_city, best_temp):

    if current_city == best_city:
        return (
            f"{current_city.title()} is one of the best choices this week 🌟\n"
            f"Would you like to explore another destination?"
        )

    return (
        f"{current_city.title()} looks great 👍\n"
        f"But {best_city.title()} is even warmer this week ({best_temp}°C) ☀️\n"
        f"Want me to show you?"
    )


# Main chatbot response
def chatbot_response(user_input):

    global last_location, awaiting_followup

    text = user_input.lower()

    # Handle "list locations"
    if text.strip() in [
        "locations",
        "what locations do you support",
        "supported locations"
    ]:
        locations_list = ", ".join([loc.title() for loc in LOCATIONS])
        return {
            "message": f"I can help with these locations: {locations_list}. Which one would you like?"
        }

    # Handle YES follow-up
    if awaiting_followup and text in ["yes", "yeah", "y"]:

        best_city, _ = get_best_destination()
        awaiting_followup = False

        if best_city:
            return chatbot_response(best_city)

        return {
            "message": "Sorry, I couldn't determine a better location right now."
        }

    # Handle NO follow-up
    if text in ["no", "n"]:
        awaiting_followup = False
        return {
            "message": "No problem! Let me know if you need anything else 😊"
        }

    # Extract city
    city = extract_location(user_input)

    if city is None:
        locations_list = ", ".join([loc.title() for loc in LOCATIONS])
        return {
            "error": f"Sorry, I can only provide weather for these locations: {locations_list}."
        }

    last_location = city

    # 🔧 FIX: handle locations OpenWeather doesn't recognise
    api_city = city
    if city == "watergate bay":
        api_city = "Newquay"

    # Get weather (with cache)
    weather_data = get_cached_weather(api_city)

    if weather_data is None:
        weather_data = get_weather(api_city)

        if weather_data:
            save_to_cache(api_city, weather_data)

    if weather_data is None:

        best_city, best_temp = get_best_destination()

        if best_city:
            return {
                "error": (
                    f"Sorry, I couldn't retrieve weather for {city.title()}.\n"
                    f"However, {best_city.title()} looks great this week ({best_temp}°C) ☀️.\n"
                    f"Would you like to check it instead?"
                )
            }

        return {
            "error": "Sorry, weather data is currently unavailable. Please try again later."
        }

    # Format forecast
    forecast_cards = []

    for day in weather_data:

        date_obj = datetime.strptime(day["date"], "%Y-%m-%d %H:%M:%S")
        formatted_day = date_obj.strftime("%A")

        forecast_cards.append({
            "day": formatted_day,
            "temperature": round(day["temperature"], 1),
            "weather": day["weather"].title(),
            "icon": day["icon"],
            "suggestion": suggest_activity(day["weather"])
        })

    # Get attraction
    attraction = get_attraction(city)

    if attraction:
        attraction_name = attraction["name"]
        attraction_map = attraction["maps"]
    else:
        attraction_name = city.title()
        attraction_map = ""

    # Smart follow-up
    best_city, best_temp = get_best_destination()
    smart_followup = generate_smart_followup(city, best_city, best_temp)

    awaiting_followup = True

    return {
        "city": city.title(),
        "forecast": forecast_cards,
        "attraction": attraction_name,
        "map": attraction_map,
        "map_query": f"{attraction_name}, {city}",
        "follow_up": smart_followup
    }


# Test
if __name__ == "__main__":
    print(chatbot_response("weather in cambridge"))
    
    