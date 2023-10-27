import os

path = r'D:\Downloads\Highschool of the Dead - Full Color Edition [Yen Press]'

for subdir, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(subdir, file))