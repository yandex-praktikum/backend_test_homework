from pprint import pprint

import requests

response = requests.get("https://swapi.dev/api/people/1/")
pprint(response.json())
