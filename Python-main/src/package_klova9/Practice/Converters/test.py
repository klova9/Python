import os
directory = 'D:\Downloads\Highschool of the Dead - Full Color Edition [Yen Press]'
for subdir, dirs, files in os.walk(directory):
    print(files)