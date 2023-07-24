import camelot
tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables)

<<<<<<<< HEAD:Python-main/Automation/Extraction/en_extract_pdf.py
tables.export('foo.csv', f='csv', compress=False)
========
tables.export('foo.csv', f='csv', compress=True)
>>>>>>>> 6681c519131bad23a5d0f316109aa26c0227b571:Python-main/src/package_klova9/Automation/ExtractPdf/en_extract_pdf.py
tables[0].to_csv('foo.csv')

