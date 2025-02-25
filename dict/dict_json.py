import json
import urllib.request

url = "https://raw.githubusercontent.com/vire/country.json/master/src/country-population.json"

response = urllib.request.urlopen(url)
data = response.read().decode()

k = json.loads(data)

print(k)


url2 = "https://raw.githubusercontent.com/vire/country.json/master/src/country-capital-city.json"

response2 = urllib.request.urlopen(url2)
data2 = response2.read().decode()

l = json.loads(data2)

print(l)