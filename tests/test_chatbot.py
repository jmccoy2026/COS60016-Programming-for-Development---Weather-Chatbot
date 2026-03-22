import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pytest
from chatbot_logic import extract_location, suggest_activity, chatbot_response


def test_extract_location_cambridge():
    result = extract_location("weather in Cambridge")
    assert result == "cambridge"


def test_extract_location_oxford():
    result = extract_location("forecast for Oxford")
    assert result == "oxford"


def test_extract_location_invalid():
    result = extract_location("weather in Paris")
    assert result is None


def test_suggest_activity_rain():
    result = suggest_activity("light rain")
    assert "museum" in result.lower() or "indoor" in result.lower()


def test_suggest_activity_clear():
    result = suggest_activity("clear sky")
    assert "outdoor" in result.lower() or "sightseeing" in result.lower()


def test_chatbot_invalid_location():
    response = chatbot_response("weather in paris")
    assert "error" in response

def test_chatbot_response_structure():
    response = chatbot_response("weather in cambridge")

    assert "city" in response
    assert "forecast" in response
    assert "attraction" in response
    assert "image" in response
    assert "map" in response