import os

root_directory = 'D:/Downloads/Highschool of the Dead - Full Color Edition [Yen Press]'
for dir, subdir, files in os.walk(root_directory):
    if files != 'Converted.pdf':
        os.remove(os.path.join(dir, subdir, files))