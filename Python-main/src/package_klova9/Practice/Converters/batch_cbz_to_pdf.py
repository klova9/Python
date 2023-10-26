import glob
import os
from PIL import Image

directory = 'C:/Users/klova9/Documents/Gate/'
pdf_path = 'D:\Python\Python-main\src\package_klova9\Practice\Converters'
subdirs = [x[0] for x in os.walk(directory)]
print(subdirs)
    #with Image.open()