from openpyxl import workbook, load_workbook

file = load_workbook('Automation\MakeCSV\grades.xlsx')
sheet = file.active
print(sheet)
