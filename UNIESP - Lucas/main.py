import requests
import json

API_KEY = "7b6b43b1bb33a616f913f59369510479"
LAT = 38.7071
LOG = -9.13549
link = f"https://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LOG}&appid={API_KEY}"

requisicao = requests.get(link)
print(requisicao.json())


response = requests.request("GET", url)
objects = json.loads(response.text)

print(objects)
print(type(objects))

for i in objects:
    print(f"{i} :: {objects[i]}")