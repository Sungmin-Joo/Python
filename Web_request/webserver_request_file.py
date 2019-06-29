# -*- coding: utf-8 -*-
import requests
import os

def Find_dir(root):
    return os.listdir(root)

url = 'http://127.0.0.1:5000/download'
response = requests.get(url = url)
print(response.status_code)
A = response.json()
print(A)
'''
arr = Find_dir("./update/word")
data = {}
for i in arr:
    f = open("./update/word/" + i,'r')
    lines = f.readlines()
    data[i] = lines
    f.close()
    
print(data)
'''