import pandas as pd
import re

data_files = [
    "Automation/SATAnalysis/schools/AP_Results.csv",
    "Automation/SATAnalysis/schools/Class_Size.csv", 
    "Automation/SATAnalysis/schools/Graduation_Outcomes.csv",
    "Automation/SATAnalysis/schools/nysd.csv",
    "Automation/SATAnalysis/schools/SAT_Results.csv",
    "Automation/SATAnalysis/schools/School_Attendanc.csv",
    "Automation/SATAnalysis/schools/School_Demographics.csv",
    "Automation\SATAnalysis\schools\Archived_DOE_High_School_Directory.csv"
]
data = ({
    'AP Results': pd.read_csv(data_files[0]),
    'Class Size': pd.read_csv(data_files[1]),
    'Graduation Outcomes': pd.read_csv(data_files[2]),
    'nysd': pd.read_csv(data_files[3]),
    'SAT Results': pd.read_csv(data_files[4]),
    'School Attendance': pd.read_csv(data_files[5]),
    'School Demographics': pd.read_csv(data_files[6]),
    'Directory': pd.read_csv(data_files[7])
})
def class_size(data):
    for row in data['Class Size']['CSD']:
        if len(str(row)) < 2:
            data['Class Size']['CSD'].replace(row, str(row).zfill(2), inplace=True)
        else:
            break
    data['Class Size']['DBN'] = data['Class Size']['CSD'].astype(str) + data['Class Size']['SCHOOL CODE']
    data['Class Size'].drop(columns=['CSD', 'SCHOOL CODE'], axis=1, inplace=True)
    
def sat_results(data):
    data['SAT Results']['Sum Mean'] = data['SAT Results'].iloc[:, [3, 4, 5]].sum(axis=1)

def directory(data):
    data['Directory']['Lat Long'] = data['Directory']['Location 1'].str.findall('\(.+\)')
    fix = re.sub(r'[\s\[()\]]', '', str(data['Directory']['Lat Long']))
    
    coord = re.split(',', fix)
    data['Directory']['Latitude'] = coord[:]
    data['Directory']['Longitude'] = coord[1]
    print(data['Directory'])
directory(data)