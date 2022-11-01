#!/usr/bin/env python3
from PIL import Image
import os, sys

path = "supplier-data/images/"
imgs = os.listdir(path)

for img in imgs:
    if 'tiff' in img:
        file_name = os.path.splitext(img)[0]
        outfile = path + file_name + ".jpeg"
        Image.open(path + img).convert('RGB').resize((600,400)).save(outfile,"JPEG")
