"""
Iterate through each file in the folder
For each file:
    -Rotate the image 90° clockwise
    -Resize the image from 192x192 to 128x128
    -Save the image to a new folder in .jpeg format
"""

from PIL import Image
import os

source_path = "Practice\Capstone_1_1\Images"
output_path = 'Practice\Capstone_1_1\Images'
for file_path in os.listdir(source_path):
    
    try:
        newfile = Image.open(os.path.join(source_path, file_path))
        newfile = newfile.resize((128,128))
        newfile= newfile.rotate(-90)
        newfile = newfile.convert('RGB')
        newfile.save(os.path.join(output_path, file_path[:-4] + '.jpg'))
        print('Succsess')
    except:
        print('Failed')

