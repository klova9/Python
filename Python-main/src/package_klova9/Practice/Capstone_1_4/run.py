#! /usr/bin/env python3

# Convert files in supplier-data/descriptions/ to JSON
# Upload following format:
#   name
#   weight (in lbs)
#   description

import os
import requests

path ='./supplier-data/descriptions/'
image_path = './supplier-data/images/'
product_dict = {}
key = ["name", "weight", "description", "image_name"]
i = 0
for file in os.listdir('./supplier-data/descriptions'):
    with open(os.path.join(path, file)) as txt:
        for lines in txt:
            line = lines.strip()
            if 'lbs' in lines:
                text = lines.split()
                weight = int(txt[0])
                product_dict['weight'] = weight
            else:
                try:
                    product_dict[key[index]] = line
                    index += 1
                except:
                    product_dict[key[2]] = line
        index = 0
        split_file = file.split(".")
        name = split_file[0] + ".jpeg"
        for file in os.listdir(image_path):
            if file == name:
                product_dict["image_name"] = name
        response = requests.post("http://35.185.84.192/fruits/", json=product_dict)
        product_dict.clear()






