import csv
# This code defines a function called read_employees that takes a parameter called csv_file_location. The function opens a CSV file located at csv_file_location and reads its data using the csv.DictReader method. It then appends each row of data to a list called employee_list aPnd returns this list.

def read_employees(csv_file_location):
    with open(csv_file_location, mode='r') as f:
        employee_file = csv.DictReader(f)
        employee_list = []
        for data in employee_file:
            employee_list.append(data)
        return employee_list
# This code takes in a list of employee data and processes it to create a dictionary of department names and the number of employees in each department.
def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Team'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
# This code defines a function called write_report that takes two arguments: a dictionary and a file path called report_file. The function opens the file specified by report_file in write mode, iterates through the keys of the dictionary in sorted order, and writes each key and its corresponding value to a new line in the file. Finally, it closes the file.
def write_report(dictionary, report_file):
     with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k)+':'+str(dictionary[k])+'\n')
        f.close() 
        
employee_list = read_employees('Python-main\Practice\Lab\employees.csv')
dictionary = process_data(employee_list)
report_file = write_report(dictionary, 'Python-main\Practice\Lab\department_report.txt')