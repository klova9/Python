import os

root_directory = 'D:/Downloads/Highschool of the Dead - Full Color Edition [Yen Press]'
subdirectorys = [x for x in os.listdir(root_directory)]

for x in subdirectorys:
    for file in os.listdir(os.path.join(root_directory, x)):
        if file != 'Converted.pdf' or file != 'Single pages':
            try:
                os.remove(os.path.join(root_directory, x, file))
            except:
                pass