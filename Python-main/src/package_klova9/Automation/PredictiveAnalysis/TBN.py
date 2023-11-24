from turtle import title
import pandas as pd

data = pd.read_csv(r'Python-main\src\package_klova9\Automation\PredictiveAnalysis\netflix_titles.csv')
print(data.head(10))
title = data['title']
type = data['type']
for i in range(len(title)):
    if type[i] == 'TV Show':
        new =data.drop(index=i, inplace=True, axis=0)
        
print(new.head(10))
    