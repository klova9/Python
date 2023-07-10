import math
import json
from tabulate import tabulate
length = 64
cost= []
product = []
length_per_unit = []
cost_per_unit = []
units = []
cost = []
with open('Python-main\FenceCost\cost.json', 'r') as f:
    data = json.load(f)
    for item in data['cost']:    
        cost.append(item['name'])
        product.append(item['product'])
        length_per_unit.append(item['length_per_unit'])
        cost_per_unit.append(item['cost_per_unit'])
    
for i, v in enumerate(length_per_unit):
    units.append(math.ceil(length / v))
for i, v in enumerate(cost_per_unit):
    cost.append(v * units[i])


table = zip(cost, product, length_per_unit, cost_per_unit, units, cost) 
with open('Python-main\FenceCost\cost_per_length.txt', 'w') as f:
    f.write(tabulate(table, headers=['cost', 'Product', 'Length Per Unit', 'Cost Per Unit', 'Total Units', 'Total Cost'], tablefmt='github', numalign='left', floatfmt=".2f"))
   