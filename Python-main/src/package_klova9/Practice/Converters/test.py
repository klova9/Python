import os

directory = 'D:\Downloads\Gate'
for subdirs, dirs, files in os.walk(directory):
    if files or dirs != 'Converted.pdf':
        print(files, dirs)