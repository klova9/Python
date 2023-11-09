import os
import send2trash

def clean_directory(directory) -> None:
    subdirs = os.listdir(directory)
    for (subdirs, dirs, files) in os.walk(directory):
            for file in files:
                path = os.path.join(subdirs, file)
                if file != 'Converted.pdf':
                    send2trash.send2trash(path)
                    print(f'{path} deleted')
            for dir in dirs:
                path = os.path.join(subdirs, dir)
                send2trash.send2trash(path)
                print(f'{path} deleted')
            