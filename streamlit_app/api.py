import requests

API_URL = "http://127.0.0.1:8000/predict"
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
    