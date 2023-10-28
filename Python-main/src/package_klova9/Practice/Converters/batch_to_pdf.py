import os
from  pypdf import PdfMerger
from PIL import Image

directory = 'D:\Downloads\Gate'
merger = PdfMerger()
for subdirs, dirs, files in os.walk(directory):
    for dir  in dirs:
        if dir != 'Single pages':
            for images in os.listdir(dir):
                if images.endswith('.jpg'):
                        img_path = os.path.join(directory, dir, images)
                        img_jpg = Image.open(img_path)
                        img_pdf = img_jpg.save(img_path[:-4]+'.pdf')
                else:
                    pass
            for pdf in os.listdir(dir):
                if pdf.endswith('.pdf'):
                    pdf_path = os.path.join(directory, dir, pdf)
                    merger.append(pdf_path)
            
merger.write(os.path.join(directory, 'Converted.pdf'))
merger.close()
