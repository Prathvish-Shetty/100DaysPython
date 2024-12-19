import requests
from datetime import datetime

MY_LAT = 18.520430
MY_LONG = 73.856743

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
# print(sunset)

time_now = datetime.now()
print(time_now)










# https://api.sunrise-sunset.org/json?lat=18.520430&lng=73.856743