import os
directory = 'D:\Downloads\Highschool of the Dead - Full Color Edition [Yen Press]'
subdir = [x for x in os.listdir(directory) ]
for subdirs, dirs, files in os.walk(directory):
    print(os.path.join(subdir[subdirs], files))