import os
from  pypdf import PdfMerger
from PIL import Image

directory = 'C:/Users/klova9/Documents/Gate/Gate - Volume 01/'
pdf_path = 'C:/Users/klova9/Documents/Gate/Convert/'
merger = PdfMerger()
i=1
for images in os.listdir(directory):
    if images.endswith('.jpg'):
        img_path = os.path.join(directory, images)
        img_jpg = Image.open(img_path)
        img_pdf = img_jpg.save(img_path[:-4]+'.pdf')
        merger.append(img_pdf)
        
merger.write('C:/Users/klova9/Documents/Gate/Gate - Volume 01/Converted.pdf')
merger.close()