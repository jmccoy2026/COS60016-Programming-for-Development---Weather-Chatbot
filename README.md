Travel Weather Chatbot

This project is a web-based chatbot that provides real-time weather forecasts and travel recommendations. Users can enter a location and receive a 5-day weather forecast, suggested activities, and a recommended attraction displayed on a map.


Features

- Retrieves real-time weather data using the OpenWeather API
- Displays a 5-day weather forecast
- Suggests activities based on weather conditions
- Recommends attractions using a SQLite database
- Interactive chatbot with follow-up questions
- Embedded map showing the selected destination


Technologies Used

- Python (Flask)
- HTML, CSS, JavaScript
- SQLite (database)
- OpenWeather API
- Requests library


Setup Instructions

To run this project locally, follow these steps:

1. Install dependencies
    pip install -r requirements.txt


2. Add your API key

    This project requires an OpenWeather API key.

    Create a file called .env in the project folder and add:

    API_KEY=your_api_key_here

    You can obtain a free API key from:
    https://openweathermap.org/


3. Run the database:
   python create.db


4. Run the application
    python app.py


5. Open in browser
    http://127.0.0.1:5000


Notes

- The .env file is not included in this repository for security reasons
- A sample file (.env.example) can be used as a reference
- Some locations may be mapped internally to ensure compatibility with the API


Project Structure

app.py
chatbot_logic.py
weather_api.py
cache.py
create_db.py
templates/
static/


GitHub Repository

(Insert your repository link here)


# Travel Weather Chatbot

This project is a web-based chatbot that provides real-time weather forecasts and travel recommendations.

## Features
- Retrieves weather data using OpenWeather API
- Displays 5-day forecast
- Suggests activities based on weather
- Recommends attractions using SQLite database
- Interactive chatbot with follow-up questions

## Technologies Used
- Python (Flask)
- HTML, CSS, JavaScript
- SQLite
- OpenWeather API

## How to Run
1. Install dependencies:
   pip install -r requirements.txt

2. Run the database:
   python create.db

2. Run the app:
   python app.py

3. Open browser:
   http://127.0.0.1:5000

## Notes
- Ensure API key is added in .env file