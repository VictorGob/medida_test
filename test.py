import json

import requests

docker = True

if docker:
    url = "http://127.0.0.1:18000/events"
else:
    url = "http://127.0.0.1:8000/events"

data = [
    {"league": "NFL", "startDate": "2024-04-01", "endDate": "2024-04-30"},
    {"league": "NFL", "startDate": "2024-04-01", "endDate": "2024-03-30"},
    {"league": "XXX", "startDate": "2024-04-01", "endDate": "2024-04-30"},
    {"param1": "value1"},
]


for d in data:
    try:
        response = requests.post(url, json=d)
        print(f"*** Response: {response.status_code=}")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"*** ERROR: {e}")
        break
