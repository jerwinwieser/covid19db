import requests
url = "https://opendata.ecdc.europa.eu/covid19/nationalcasedeath/json/"
r = requests.get(url=url)
print(r.json())
