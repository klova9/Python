import os
from  pypdf import PdfMerger
from PIL import Image
import zipfile

directory = 'D:\Downloads\Claymore (v01-v27) (2006-2015) (Digital) (LostNerevarine-Empire)'
merger = PdfMerger()
for subdirs, dirs, files in os.walk(directory):
    for dir  in dirs:
        if dir[:-4] == '.cbz':
            with zipfile.ZipFile(os.path.join(directory, dir), 'r'):
                zip(directory)
            
        if dir != 'Single pages':
            for images in os.listdir(os.path.join(directory, dir)):
                if images.endswith('.jpg'):
                        img_path = os.path.join(directory, dir, images)
                        img_jpg = Image.open(img_path)
                        img_pdf = img_jpg.save(img_path[:-4]+'.pdf')
                        print(f'{img_path} converted')
                else:
                    pass
            for pdf in os.listdir(os.path.join(directory, dir)):
                if pdf.endswith('.pdf'):
                    pdf_path = os.path.join(directory, dir, pdf)
                    merger.append(pdf_path)
                    print(f'{pdf_path} appended')   
            
print('Merging PDFs...')
merger.write(os.path.join(directory, 'Converted.pdf'))
print('Done!')
merger.close()

