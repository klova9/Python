import os
from  pypdf import PdfMerger
from PIL import Image

directory = r'D:\Downloads\Highschool of the Dead - Full Color Edition [Yen Press]'
subdirectory = [x for x in os.listdir(directory)]
[print(os.path.join(directory,x)) for x in subdirectory]