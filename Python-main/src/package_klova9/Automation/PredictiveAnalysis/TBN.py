import pandas as pd

data = pd.read_csv(r'Automation\PredictiveAnalysis\netfilx_titles.csv')
data_frame = pd.DataFrame(data)
#data_frame.drop(data_frame[data_frame['type'] == 'TV Show'].index, inplace=True)
data_frame[['genre1', 'genre2', 'genre3']] = data_frame['Genre'].str.split(',', expand=True)
data_frame.drop(columns=['Genre'], axis=1, inplace=True)

group1 = data_frame.groupby(['genre1'])
group2 = data_frame.groupby(['genre2'])
group3 = data_frame.groupby(['genre3'])
pd.options.display.float_format = '${:,.2f}m'.format
print(group1['Revenue (Millions)'].mean())
print(group2['Revenue (Millions)'].mean())
print(group3['Revenue (Millions)'].mean())