import json

with open("states.json", "r") as f:
    data = json.load(f)

    # Extracting all data from json
    for state in data['states']:
        print(state)

    # Extracting specific data from json using key
    for state in data['states']:
        print(state['name'], state['abbreviation'])

    # Remove specific data from json
    for state in data['states']:
        del state['area_codes']
with open("new_json","w") as wf:
    json.dump(data, wf, indent=2)



