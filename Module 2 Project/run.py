#!/usr/bin/env python3
import requests 
import os

path = '/data/feedback/'
list_files = os.listdir(path)

for file in list_files:
    dict_feedback = {}
    fh = open(path + file, 'r')
    text = fh.readlines()
    dict_feedback['title'] = text[0].strip()
    dict_feedback['name'] = text[1].strip()
    dict_feedback['date'] = text[2].strip()
    dict_feedback['feedback'] = text[3].strip()
    response = requests.post("http://34.70.14.157/feedback/", data=dict_feedback)   
    response.raise_for_status()
    fh.close()

