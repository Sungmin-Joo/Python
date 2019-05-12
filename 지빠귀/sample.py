# -*- coding: utf-8 -*-
import requests

url = 'https://maker.ifttt.com/trigger/abc/with/key/ewP4WjeyqlkpW833vBEsLgiQWUbc-lLZ2NQw5vSkCYB'
response = requests.get(url = url)
print(response.status_code)
print(response.text)

