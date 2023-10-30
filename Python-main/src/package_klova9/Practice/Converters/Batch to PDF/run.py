import extract
import batch_to_pdf
import clean_directory

extract.extract()
batch_to_pdf.convert()
clean_directory.clean_directory()

print('All Done!')