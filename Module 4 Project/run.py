#! /usr/bin/env python3
import os
from urllib import request
import requests

url = 'http://146.148.49.166/fruits/'
path = "supplier-data/descriptions/"
list_textfiles = os.listdir(path)

for txt_file in list_textfiles:
    if txt_file.endswith('.txt'):
        with open(path + txt_file, 'r') as fh:
            content = fh.readlines()
            name =  content[0].strip()
            weight = int(content[1].strip().split(" lbs")[0])
            description = content[2].strip()
            image_name = os.path.splitext(txt_file)[0] + ".jpeg"
            dictionary = {'name': name, 'weight': weight, 'description': description, 'image_name': image_name}
            response = requests.post(url, data=dictionary)
            response.raise_for_status()
