import glob
import os
from PIL import Image

directory = 'C:/Users/klova9/Documents/Gate/'
pdf_path = 'D:\Python\Python-main\src\package_klova9\Practice\Converters'
# If directory contains multiple subdirectories
subdirs = [x[0] for x in os.walk(directory)]
if len(subdirs) > 1:
    for subdir in subdirs:
        print(subdir)


#print(subdirs)
    #with Image.open()