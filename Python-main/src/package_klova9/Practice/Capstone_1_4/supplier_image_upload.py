#!/usr/bin/env python3
import requests
import os

url = "http://localhost/upload/"
path = './supplier-data/images/'
for file in os.listdir(path):
    if file.endswith('.jpeg'):
        with open(os.path.join(path, file), 'rb') as opened:
            r = requests.post(url, files={'file': opened})
    