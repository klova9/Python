import os

path = 'D:/Downloads/[Pajeet] Battle Royale'
subfolders = [d for d in os.listdir(path)]
for folder in subfolders:
    print(subfolders[folder])