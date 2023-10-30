import zipfile
import os
directory = 'd:\Downloads\Kaifuku Jutsushi no Yarinaoshi'
def un_zipFiles(directory):
    files=os.listdir(directory)
    for file in files:
        if file.endswith('.cbz'):
            filePath=directory+'/'+file
            zip_file = zipfile.ZipFile(filePath)
            for names in zip_file.namelist():
                zip_file.extract(names,directory)
            zip_file.close() 