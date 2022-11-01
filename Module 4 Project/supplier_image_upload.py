#!/usr/bin/env python3
import os
import requests

url = "http://localhost/upload/"
path = "supplier-data/images/"
img_list = os.listdir(path)

for img in img_list:
    if img.endswith('.jpeg'):
        with open(path + img, 'rb') as fh:
            requests.post(url, files={'file':fh})

