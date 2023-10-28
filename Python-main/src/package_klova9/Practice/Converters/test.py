import os
import send2trash
from batch_to_pdf import directory
directory = directory
subdirs = os.listdir(directory)

for (subdirs, dirs, files) in os.walk(directory):
    if (dirs, files) != 'Converted.pdf':
        for file in files:
            path = os.path.join(subdirs, file)
            send2trash.send2trash(path)
            print(f'{path} deleted')
        for dir in dirs:
            path = os.path.join(subdirs, dir)
            send2trash.send2trash(path)
            print(f'{path} deleted')
    
#for subdirs, dirs, files in os.walk(directory):
"""if files or subdirs != 'Converted.pdf':
    for file in files:
        os.remove(os.path.join(file))"""