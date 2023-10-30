import zipfile
import os

def extract(directory):
    subdirs = [x for x in os.listdir(directory)]
    for (subdirs, dirs, files) in os.walk(directory):
        for file in files:
            if file.endswith('.cbz'):
                path = os.path.join(subdirs, file)
                extracted = zipfile.ZipFile(path).extractall(directory)
                print(f'{path} extracted')