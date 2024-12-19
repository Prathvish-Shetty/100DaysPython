import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("api_key")
account_sid = os.getenv("account_sid")
auth_token = os.getenv("auth_token")

weather_params = {
    "lat": 18.520430,
    "lon": 73.856743,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0])
will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an Umbrella☔",
        from_='+14159157823',
        to='+917276229611'
    )
    print(message.status)

# environment variables
# python3 basic.py

# plist.fun
