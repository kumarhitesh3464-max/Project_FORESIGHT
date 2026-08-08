import requests

API_URL = "https://project-foresight-gs0h.onrender.com/predict"


def get_prediction(data):
    try:
        response = requests.post(API_URL, json=data)

        if response.status_code == 200:
            return response.json()

        return {
            "error": response.text
        }

    except Exception as e:
        return {
            "error": str(e)
        }