import extract
import batch_to_pdf
import clean_directory
directory = r'C:\Users\klova9\Documents\Highschool of the Dead - Full Color Edition [Yen Press]'
extract.extract(directory)
batch_to_pdf.convert(directory)
clean_directory.clean_directory(directory)

print('All Done!')