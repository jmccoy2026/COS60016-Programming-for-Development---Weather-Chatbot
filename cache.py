from datetime import datetime, timedelta

# Store cached weather results
weather_cache = {}

# Cache expiry time
CACHE_DURATION = timedelta(minutes=10)


def get_cached_weather(city):

    city = city.lower()

    if city in weather_cache:

        data, timestamp = weather_cache[city]

        if datetime.now() - timestamp < CACHE_DURATION:
            return data
        else:
            del weather_cache[city]

    return None


def save_to_cache(city, data):

    city = city.lower()

    weather_cache[city] = (data, datetime.now())