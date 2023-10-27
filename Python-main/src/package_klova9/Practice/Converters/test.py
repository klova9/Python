import os
from  pypdf import PdfMerger
from PIL import Image

directory = r'D:\Downloads\Highschool of the Dead - Full Color Edition [Yen Press]'
subdirectory = [x for x in os.listdir(directory)]

for x in subdirectory:
    directory = os.path.join(directory, subdirectory[x])
    print(os.path.join(directory))