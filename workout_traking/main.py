import requests
import datetime
import os
print(os.environ)
APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'


user_input = input("Tell me which exercises you did: ")
exercise_params = {
    "query": user_input,
    "gender": "female",
    "weight_kg": 67.5,
    "height_cm": 174.5,
    "age": 31
}

exercise_header = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_params, headers=exercise_header)
response.raise_for_status()
data = response.json()

sheety_endpoint = "https://api.sheety.co/791b9114d181bc5cbb671905412a4c52/workoutTracking/sheet1"
today = datetime.datetime.now()

sheety_header = {
    'Authorization': os.environ["AUT_BEARER"],
}


today_date = datetime.datetime.now().strftime("%d/%m/%Y")
now_time = datetime.datetime.now().strftime("%X")

for exercise in data["exercises"]:
    sheet_inputs = {
        "sheet1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_header)

    print(sheet_response.text)


