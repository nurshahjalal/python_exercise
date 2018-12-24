import json
import requests
import urllib3


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


baseUrl = 'https://dev-api.sandata.com/interfaces/intake/clients/rest/api/v1'

with open("client.json", "r") as f:
    json_data = json.load(f)
    json_body = json.dumps(json_data)

    headers = {
        'Account': "28007",
        'Content-Type': "application/json",
        'cache-control': "no-cache",
        'Postman-Token': "c9045c0b-3ea3-4039-8c72-c5a9dd3f1fcd"
    }

    response = requests.request("POST", baseUrl, auth=('kjon784FH', 'DG4867Fsu'), data=json_body, headers=headers,verify=False)
    d = response.json()
    print(response)
    print(d['id'])
    print(response.text)
    print(type(response.content))



    # for item in response.text:
    #     print(item)

    # s = requests.post(baseUrl, auth=('kjon784FH', 'DG4867Fsu'), verify=False, json=data)
    # print(s.status_code)
