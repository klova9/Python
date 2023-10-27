for dir, subdir, files in os.walk(directory):
    if files != 'Converted.pdf':
        os.remove(os.path.join(dir, subdir, files))