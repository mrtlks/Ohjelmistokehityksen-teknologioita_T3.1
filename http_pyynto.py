import urllib.request
import json

#käytössä malliratkaisun http_pyyntö.py
def hae_postinumerot():
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        data = response.read()

    postinumerot = json.loads(data)
    return postinumerot
