import extract
import batch_to_pdf
import clean_directory
directory = 'directory'
extract.extract(directory)
batch_to_pdf.convert(directory)
clean_directory.clean_directory(directory)

print('All Done!')