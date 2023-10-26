import glob
import os
from PIL import Image

directory = 'C:/Users/klova9/Documents/Gate/'
pdf_path = 'D:\Python\Python-main\src\package_klova9\Practice\Converters'
# If directory contains multiple subdirectories
def convert_file(directory, pdf_path):
    subdirs = [x[0] for x in os.walk(directory)]
    if len(subdirs) > 1:
        for subdir in subdirs:
            with Image.open(subdir) as img:
                img.save(pdf_path, "PDF", save_all=True)
    #else:
    
paths = glob.glob('*.jpg')
for path in paths:
    convert_file(path, path[:-4] + '.pdf')
#print(subdirs)
    #with Image.open()