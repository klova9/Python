import os
from PIL import Image
directory = 'C:/Users/klova9/Documents/Gate/'
for path, subdirs, files in os.walk(directory):
    images = [ Image.open(os.path.join(path, name)) for name in files ]
    print(len(images))
    
            
