import os
from PIL import Image

directory = 'C:/Users/klova9/Documents/Gate/Gate - Volume 01'
pdf_path = 'C:/Users/klova9/Documents/Gate/Convert'
# If directory contains multiple subdirectories

for images in os.listdir(directory):
    if images.endswith('.jpg'):