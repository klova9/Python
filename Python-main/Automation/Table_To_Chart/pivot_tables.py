import pandas as pd

df = pd.read_excel('Python-main\Automation\Table_To_Chart\supermarket_sales.xlsx')
df = df[['Gender', 'Product line', 'Total']]
pivot_table = df.pivot_table(index='Gender', columns='Product line', values='Total', aggfunc='sum').round(0)
#print(pivot_table)\
pivot_table.to_excel('pivot_table.xlsx', 'Report', startrow=4)