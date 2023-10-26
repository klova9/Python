import os

directory = 'D:/Python/Python-main/src/package_klova9/Practice/Labs/'
subdirectories = [x[0] for x in os.walk(directory)]
for subdirectory in subdirectories:
    print(f'{subdirectory}')