import os

directory = 'D:\Downloads\Gate'
subdirs= os.listdir(directory)
files = []
for x in subdirs:
    files.append(x)
print(files)
#for subdirs, dirs, files in os.walk(directory):
"""if files or subdirs != 'Converted.pdf':
    for file in files:
        os.remove(os.path.join(file))"""