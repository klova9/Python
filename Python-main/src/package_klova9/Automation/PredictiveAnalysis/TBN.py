from turtle import title
import pandas as pd

data = pd.read_csv(r'Python-main\src\package_klova9\Automation\PredictiveAnalysis\netflix_titles.csv')
print(data.head(10))
title = data['title']
type = data['type']
print(type)
    