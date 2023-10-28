import os

directory = 'D:\Downloads\Gate'
for subdirs, dirs, files in os.walk(directory):
    if files or dirs != 'Converted.pdf':
        os.remove(os.path.join(directory, dirs, files))