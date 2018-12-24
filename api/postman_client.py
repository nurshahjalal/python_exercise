import requests
import certifi

certifi.where()
url = "https://dev-api.sandata.com/interfaces/intake/clients/rest/api/v1"

payload = "[{\r\n      \"ProviderIdentification\": \r\n      { \"ProviderID\": \"28007\",\r\n      \"ProviderQualifier\": \"Other\"},\r\n      \"ClientID\": \"7109945\",\r\n      \"ClientFirstName\": \"Abbas\",\r\n      \"ClientMiddleInitial\": \"H\",\r\n      \"ClientLastName\": \"Jelly\",\r\n      \"PayerName\": \"ODM\",\r\n      \"ClientQualifier\": \"ClientCustomID\",\r\n      \"ClientMedicaidID\": \"78670092341\",\r\n      \"ClientIdentifier\": \"7170995001\",\r\n      \"SequenceID\": \"80014457\",\r\n      \"ClientCustomID\": \"423001\",\r\n      \"ClientOtherID\": \"68334\",\r\n      \"ClientSSN\": \"192807894\",\r\n      \"ClientTimezone\": \"US/Eastern\",\r\n      \"ClientAddress\": [\r\n         {\r\n            \"ClientAddressType\": \"Home\",\r\n            \"ClientAddressIsPrimary\": \"true\",\r\n            \"ClientAddressLine1\": \"36 West 5th Street\",\r\n            \"ClientAddressLine2\": \"10th Floor\",\r\n            \"ClientCounty\": \"Kings\",\r\n            \"ClientCity\": \"Manhattan\",\r\n            \"ClientState\": \"NY\",\r\n            \"ClientZip\": \"10017\",\r\n            \"ClientAddressLongitude\": \"30.98\",\r\n            \"ClientAddressLatitude\": \"40.09\"\r\n            \r\n         }\r\n      ],\r\n      \"ClientPhone\": [\r\n         {\r\n            \"ClientPhoneType\": \"Home\",\r\n            \"ClientPhone\": \"2123459099\"\r\n         }\r\n      ],\r\n\t\"ClientPayerInformation\": [\r\n\t      {\r\n        \"PayerID\": \"TC95821\",\r\n        \"PayerProgram\": \"TC95824\",\r\n        \"ProcedureCode\": \"HHA\"\r\n      }],\r\n      \"ClientResponsibleParty\": [\r\n         {\r\n            \"ClientContactType\": \"Family\",\r\n            \"ClientContractFirstName\": \"DavidhujdyDavidhRujdyDavidhujdy\",\r\n            \"ClientContactLastName\": \"Rutgos\",\r\n            \"ClientContactPhoneType\": \"Mobile\",\r\n            \"ClientContactPhone\": \"3478788467\",\r\n            \"ClientContactEmailAddress\": \"DavidD@sandata.com\",\r\n            \"ClientContactAddressLine1\": \"7 East 29th Street\",\r\n            \"ClientContactAddressLine2\": \"Apt 8I\",\r\n            \"ClientContactCity\": \"Brooklyn\",\r\n            \"ClientContactState\": \"NY\",\r\n            \"ClientContactZip\": \"11229\"\r\n         }\r\n      ]\r\n   }\r\n]"
headers = {
    'Account': "28007",
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "c9045c0b-3ea3-4039-8c72-c5a9dd3f1fcd"
    }

response = requests.request("POST", url, data=payload, headers=headers,verify=False)

print(response.text)