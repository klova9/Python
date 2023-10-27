import os

path = r'D:\Downloads\Highschool of the Dead - Full Color Edition [Yen Press]'

for subdir, dirs in os.walk(path):
    for subdir in dir:
        print(os.path.join(subdir))