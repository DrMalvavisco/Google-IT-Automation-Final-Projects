#!/urs/bin/env python3
import os
from PIL import Image
cwd = os.getcwd()
path = cwd + '/images/'
files_list = os.listdir(path)
save_path = cwd + '/images_transformed/' #/opt/icons/

for file in files_list:
    if not file.startswith('.'):
        Image.open(path + file).rotate(270).resize((128,128)).convert('RGB').save(save_path + 'fr_' + file + '.jpg', 'JPEG')
