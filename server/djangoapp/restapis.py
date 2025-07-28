import requests
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

backend_url = os.getenv('backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/"
)


def get_request(endpoint, **kwargs):
    """Make GET request to backend"""
    params = ""
    if kwargs:
        for key, value in kwargs.items():
            params = params + key + "=" + value + "&"

    request_url = backend_url + endpoint + "?" + params
    print("GET from {} ".format(request_url))
    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
        return None


def analyze_review_sentiments(text):
    """Analyze sentiment of review text"""
    try:
        encoded_text = urllib.parse.quote(text)
        request_url = sentiment_analyzer_url + "analyze/" + encoded_text
        print(f"Sentiment analysis request: {request_url}")

        response = requests.get(request_url, timeout=10)
        result = response.json()
        print(f"Sentiment response: {result}")
        return result
    except Exception as err:
        print(f"Sentiment analysis error: {err}")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    """Post review to backend"""
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        print(response.json())
        return response.json()
    except Exception as e:
        print(f"Network exception occurred: {e}")
        return None
