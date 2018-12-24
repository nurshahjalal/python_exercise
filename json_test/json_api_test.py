import json
from urllib.request import urlopen

with urlopen("https://samples.openweathermap.org/data/2.5/history/city?id=2885679&type="
             "hour&appid=b1b15e88fa797225412429c1c50c122a1") as response:
    source = response.read()
    data = json.loads(source)
    print(json.dumps(data, indent=2))

    print("#" *30)
    for item in data['list']:
        print(item['main']['temp'])

