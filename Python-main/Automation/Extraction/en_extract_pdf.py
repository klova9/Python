import camelot
tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables)

tables.export('foo.csv', f='csv', compress=False)
tables[0].to_csv('foo.csv')

