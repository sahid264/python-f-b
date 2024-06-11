import requests
from datetime import datetime

USER_NAME = "sahid"
TOKEN = "skr1234skr"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username":USER_NAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",

}

# response = requests.post(url= pixela_endpoint, json=user_params)

# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config ={
    "id":GRAPH_ID,
    "name":"Cycling graph",
    "unit":"km",
    "type":"float",
    "color":"sora"
}

header={
    "X-USER-TOKEN":TOKEN

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

post_creation_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"

today = datetime.now()


header={
    "X-USER-TOKEN":TOKEN

}

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many kilometer did you cycle today?"),
    
}

# response = requests.post(url=post_creation_endpoint, json=pixel_data, headers=header)
# print(response.text)

update_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

new_pixel_data= {
    "quantity":"4.5"
}

# response = requests.put(url=update_endpoint, json=new_pixel_data, headers=header)

# print(response.text)

delete_endpoint =f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text) 

