import os
from  pypdf import PdfMerger
from PIL import Image

directory = 'D:/Downloads/Highschool of the Dead - Full Color Edition [Yen Press]'
subdirectorys = [x for x in os.listdir(directory)]

merger = PdfMerger()
i=1
for x in subdirectorys:
    directory = os.path.join(directory, x)
    for images in os.listdir(directory):
        if images.endswith('.jpg'):
            img_path = os.path.join(directory, images)
            img_jpg = Image.open(img_path)
            img_pdf = img_jpg.save(img_path[:-4]+'.pdf')
    else:
        pass

    for pdf in os.listdir(directory):
        if pdf.endswith('.pdf'):
            pdf_path = os.path.join(directory, pdf)
            merger.append(pdf_path)

merger.write(os.path.join(directory, 'Converted.pdf'))
merger.close()