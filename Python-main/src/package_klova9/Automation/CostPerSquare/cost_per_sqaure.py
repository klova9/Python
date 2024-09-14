import math
from tabulate import tabulate
import json
#This code calculates the cost of using a product based on the area per unit, cost per unit, and the dimensions of the product. It loads data from a JSON file containing information about manufacturers and their products, then calculates the number of units needed to use the product based on the total area of a room. Finally, it outputs a table with the manufacturer name, product name, area per unit, cost per unit, total number of units required, and the total cost.
#All this code was writted by me in 6 hours as a personal project to decide what floor type I would like to use in by basement.


lengh = 26
width = 13
area = lengh * width
manufacturer= []
product = []
area_per_unit = []
cost_per_unit = []
units = []
cost = []
with open('D:\Python\Python-main\src\package_klova9\Automation\CostPerSquare\manufacturer_list.json', 'r') as f:
    data = json.load(f)
    for item in data['manufacterure']:    
        manufacturer.append(item['name'])
        product.append(item['product'])
        area_per_unit.append(item['area_per_unit'])
        cost_per_unit.append(item['cost_per_unit'])
    
for i, v in enumerate(area_per_unit):
    units.append(math.ceil(area / v))
for i, v in enumerate(cost_per_unit):
    cost.append(v * units[i])


table = zip(manufacturer, product, area_per_unit, cost_per_unit, units, cost) 
with open('D:\Python\Python-main\src\package_klova9\Automation\CostPerSquare\cost_per_sqaure.txt', 'w') as f:
    f.write(tabulate(table, headers=['Manufacturer', 'Product', 'Area Per Unit', 'Cost Per Unit', 'Total Units', 'Total Cost'], tablefmt='github', numalign='left', floatfmt=".2f"))
   