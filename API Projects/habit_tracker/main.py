import requests
from datetime import datetime
USER_NAME = "jeffreyli9282"
TOKEN = "lijiawei8010179"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "lijiawei8010179",
    "username": "jeffreyli9282",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Graph",
    "unit": "Projects",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response)

datetime_now = datetime.now()

graph_post_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1"

graph_post_params = {
    "date": "20230906",
    "quantity": "3.5"
}

# response = requests.post(url=graph_post_endpoint, json=graph_post_params, headers=headers)
# print(response)

graph_put_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/graph1/20230906"
graph_put_params = {
    "quantity": "10"
}
# response = requests.put(url=graph_put_endpoint, json=graph_put_params, headers=headers)
# print(response)

# response = requests.delete(url=graph_put_endpoint, headers=headers)
# print(response.text)
