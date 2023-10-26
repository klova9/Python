import os

directory = 'D:/Python/Python-main/src/package_klova9/Practice/Labs/'
subdirectories = [os.listdir(directory)]

    
files = []
for subdirectory in subdirectories:
    for file in subdirectory:
        
        files.append(file)

print(files)