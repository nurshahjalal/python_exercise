import json

with open("client.json", "r") as f:
    json_data = json.load(f)

    print(json_data['ClientID'])

