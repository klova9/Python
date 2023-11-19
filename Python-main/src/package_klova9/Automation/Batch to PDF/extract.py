import zipfile
import os

def extract(directory):
    subdirs = os.listdir(directory)
    for (subdirs, files) in os.walk(directory):
        for file in files:
            if str(file).endswith ('.cbz'):
                path = os.path.join(subdirs, file)
                zipfile.ZipFile(path).extractall(directory)
                print(f'{path} extracted')
    