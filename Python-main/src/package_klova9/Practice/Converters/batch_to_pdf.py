import os
from  pypdf import PdfMerger
from PIL import Image

directory = r'C:\Users\klova9\Documents'



subfolders = [d for d in os.listdir(directory)]
for subfolder in subfolders:
    merger = PdfMerger()
    for images in os.listdir(directory):
        if images.endswith('.jpg'):
            img_path = os.path.join(directory, images)
            img_jpg = Image.open(img_path)
            img_pdf = img_jpg.save(img_path[:-4]+'.pdf')

    for pdf in os.listdir(directory):
        if pdf.endswith('.pdf'):
            pdf_path = os.path.join(directory, pdf)
            merger.append(pdf_path)

    merger.write(os.path.join(directory, 'Converted.pdf'))
    merger.close()