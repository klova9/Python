import zipfile
import os
directory = 'd:\Downloads\Kaifuku Jutsushi no Yarinaoshi'

subdirs = [x for x in os.listdir(directory)]
for (subdirs, dirs, files) in os.walk(directory):
    