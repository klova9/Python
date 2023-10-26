import os
from  pypdf import PdfMerger
from PIL import Image

directory = 'C:/Users/klova9/Documents/Gate/Gate - Volume 01/'
subdirecrtory = [x[0] for x in os.walk(directory)]
merger = PdfMerger()
i=1
for subdir in subdirecrtory:
    for images in os.listdir(subdir):
        if images.endswith('.jpg'):
            img_path = os.path.join(directory, images)
            img_jpg = Image.open(img_path)
            img_pdf = img_jpg.save(img_path[:-4]+'.pdf')

    for pdf in os.listdir(subdir):
        if pdf.endswith('.pdf'):
            pdf_path = os.path.join(subdir, pdf)
            merger.append(pdf_path)

    merger.write('C:/Users/klova9/Documents/Gate/Gate - Volume 01/Converted.pdf')
    merger.close()