import os
directory = 'D:/Python/Python-main/src/package_klova9/Practice/Labs/'
for path, subdirs, files in os.walk(directory):
    for name in files:
        if name.endswith(".log"):
            print(os.join(subdirs,name))