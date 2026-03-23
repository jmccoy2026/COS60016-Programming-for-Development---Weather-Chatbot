from flask import Flask, render_template, request, jsonify

from chatbot_logic import (
    chatbot_response,
    get_best_destination,
    get_weather_rating
)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/best")
def best_destination():

    city, temp = get_best_destination()
    rating = get_weather_rating(temp)

    return jsonify({
        "city": city.title(),
        "temperature": temp,
        "rating": rating
    })


@app.route("/chat", methods=["POST"])
def chat():

    try:
        user_message = request.json.get("message")

        if not user_message:
            return jsonify({"error": "Please enter a location."})

        response = chatbot_response(user_message)

        return jsonify(response)

    except Exception:
        return jsonify({"error": "Something went wrong processing your request."})


if __name__ == "__main__":
    app.run(debug=True)