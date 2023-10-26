import os

directory = 'D:/Python/Python-main/src/package_klova9/Practice/Labs/'
subdirectories = [os.listdir(directory)]
for subdirectory in subdirectories:
    print(f'{subdirectory}')
    
files = []
for file in os.walk[os.join(directory, subdirectory)]:
    files.append(file)

print(files)