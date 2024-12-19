# An Application Programming Interface(API) is a set of commands, functions, protocols, and objects
# that programmers can use to create software or interact with an external system
# It is an interface between you program and external system
# request and response

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
response.raise_for_status()

data = response.json()
position = response.json()["iss_position"]
longitude = position["longitude"]
latitude = position["latitude"]
iss_position = (latitude, longitude)
print(data)
print(position)
print(iss_position)
# if response.status_code != 200:
#     raise Exception("Bad response from ISS API")
#
# if response.status_code == 404:
#     raise Exception("You are not authorised to access this data")

# 1XX: Hold on
# 2XX: Here you go
# 3XX: Go Away
# 4XX: You screwed up
# 5XX: I screwed up
# https://www.webfx.com/web-development/glossary/http-status-codes/
# latlong.net