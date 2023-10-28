import os
directory = 'D:\Downloads\Highschool of the Dead - Full Color Edition [Yen Press]'
subdir = [x for x in os.listdir(directory) ]
for subdirs, dirs, files in os.walk(directory):
    for dir  in dirs:
        if dir != 'Single pages':
            print(os.path.join(directory, dir))