import json
import requests
from bs4 import BeautifulSoup


baseurl = 'https://reqres.in'

response = requests.get(baseurl + '/api/users?page=2')
print(response)

if response.status_code == 200:
    print("successful with message " + response.status_code)
data = response.json()
print(json.dumps(data, indent=2))

session = requests.session()

