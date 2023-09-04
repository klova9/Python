#! /usr/bin/env python3
import os
import requests
dir = '/data/feedback/'
files = os.listdir(dir)
url = "http://localhost/feedback/"

def read_files():
    for file in files:
        feedback = {}
        with open(os.path.join(dir, file)) as f:
            lines = f.readlines()
            feedback['title'] = lines[0].strip()
            feedback['name'] = lines[1].strip()
            feedback['date'] = lines[2].strip()
            feedback['feedback'] = lines[3].strip()
        response = requests.post("http://35.197.114.215/feedback/", json=feedback)
        if not response.ok:
            raise Exception(f'Fail {response.status_code}')
        print("Success")
read_files()