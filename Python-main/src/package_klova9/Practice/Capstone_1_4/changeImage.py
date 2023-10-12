#!/usr/bin/env python3
# Change image resolution from 3000x2000 to 600x400 pixel
# Change image format from .TIFF to .JPEG

from PIL import Image
import os

path = './supplier-data/images/'
for file in os.listdir(path):
    if file.endswith('.tiff'):
        try:
            new_file = Image.open(os.path.join(path, file))
            new_file = new_file.convert('RGB')
            new_file = new_file.resize((600, 400))
            split_fILE = file.split(".")
            name = split_fILE[0] + ".jpeg"
            new_file.save('./supplier-data/images/' + name, 'JPEG')
            print('Succsess')
        except:
            print(file + ' Failed')
