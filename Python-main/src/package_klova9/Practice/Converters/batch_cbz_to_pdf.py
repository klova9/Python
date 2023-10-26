import os
directory = 'C:\Users\klova9\Documents\Gate'
for path, subdirs, files in os.walk(directory):
    for name in files:
        if name.endswith(".jpg"):
            print(f'{path}/{name}')