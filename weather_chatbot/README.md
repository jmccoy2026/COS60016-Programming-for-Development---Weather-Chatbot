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

2. Run the database:
   python create.db


3. Run the application
    python app.py


4. Open in browser
    http://127.0.0.1:5000



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
- Conversation Example
   "What is the weather in Oxford?"
   "Yes"
   "No"