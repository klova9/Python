import os
import send2trash

directory = 'D:\Downloads\Gate'
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