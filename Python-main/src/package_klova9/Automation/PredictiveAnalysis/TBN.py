from turtle import title

import pandas as pd

data = pd.read_csv(r'Python-main\src\package_klova9\Automation\PredictiveAnalysis\netflix_titles.csv')
data_frame = pd.DataFrame(data)
for i in data_frame['type']:
    if data_frame['type'][i] != 'Movie':
        data_frame.drop(data_frame['type'][i], inplace=True, axis=0)
        
print(data_frame)
    