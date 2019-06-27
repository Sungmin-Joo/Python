# -*- coding: utf-8 -*-
import requests

url = 'http://127.0.0.1:5000/shutdown'
response = requests.get(url = url)
print(response.status_code)
print(response.text)

