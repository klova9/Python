import os
from  pypdf import PdfMerger
from PIL import Image

directory = r'C:\Users\klova9\Documents'
subdirectories = [d for d in os.listdir(directory)]

i=1
def pdf_to_jpg(subdirectory):
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
    
for subdirectory in subdirectories:
    pdf_to_jpg(subdirectory)