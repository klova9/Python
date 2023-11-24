from progress.bar import Bar
import pandas as pd

data = pd.read_csv(r'Python-main\src\package_klova9\Automation\PredictiveAnalysis\netflix_titles.csv')
data_frame = pd.DataFrame(data)
with Bar('Processing...') as bar:
    for i in data_frame['type']:
        if i != 'Movie':
            data_frame.drop(data_frame['type'].index, inplace=True, axis=0)
        bar.next()
        
print(data_frame)
    