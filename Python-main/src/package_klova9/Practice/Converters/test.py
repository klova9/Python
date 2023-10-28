import os
import send2trash

directory = 'D:\Downloads\Gate'
subdirs = os.listdir(directory)
print(subdirs)
res = []
for (subdirs, dirs, files) in os.walk(directory):
    if (dirs, files) != 'Converted.pdf':
        for file in files:
            send2trash.send2trash(os.path.join(subdirs, file))
            print
    
#for subdirs, dirs, files in os.walk(directory):
"""if files or subdirs != 'Converted.pdf':
    for file in files:
        os.remove(os.path.join(file))"""