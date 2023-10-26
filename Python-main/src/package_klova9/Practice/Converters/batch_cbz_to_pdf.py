import os
from PIL import Image
directory = 'C:/Users/klova9/Documents/Gate/'
pdf_path = 'D:\Python\Python-main\src\package_klova9\Practice\Converters'
for path, subdirs, files in os.walk(directory):
    images = [ Image.open(os.path.join(path, name)) for name in files ]
    images.save(pdf_path, "PDF")
    
            
