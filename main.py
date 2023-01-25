import requests
import json

response = requests.get("http://universities.hipolabs.com/search?country=latvia")
pod = (json.dumps(response.json(), indent=4, sort_keys=True ))
response_json = json.loads(pod)
pip = (sorted(response_json, key=lambda names: names['name'])) 
print(pip)
print("---------------------------------------------------------------------")
get_list = []
for get in pip:
   get_list.append(get["name"])
for get in get_list:
  print(get)