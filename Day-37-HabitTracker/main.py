import requests
from datetime import datetime

USERNAME = "pss"
TOKEN = "1e28xblifvu"
GRAPH_ID = "graph1"

# setting up a user account in pixela

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": "1e28xblifvu",
    "username": "pss",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# https://pixe.la/@pss
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# print(response.json())

# create a new graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Study Graph",
    "unit": "hr",
    "type": "float",
    "color": "shibafu"
}

# authenticate ourselves using header
headers = {
    "X-USER-TOKEN": TOKEN
}

# create graph

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# https://pixe.la/v1/users/a-know/graphs8
# https://pixe.la/v1/users/pss/graphs/graph1.html

today = datetime.now()

# print(today.strftime("%Y%m%d"))
# today = datetime(year=2024, month=8, day=24)

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you studied today?")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "10"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
