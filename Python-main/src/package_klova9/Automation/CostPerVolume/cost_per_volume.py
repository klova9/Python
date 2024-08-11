# Calculate cubic area of a toroid
# Determine units of material required to build toroid
# Determine cost of material required to build toroid
import json
import math
from tabulate import tabulate

x = 2 # Diameter of inner circle
y = 4 # Diameter of outer circle
z = 0.5 # Height of cylinder

# Volume of outer cylinder
v1 = math.pi * math.pow(y/2, 2) * z
# Volume of inner cylinder
v2 = math.pi * math.pow(x/2, 2) * z
# Volume of toroid
v = v1 - v2

# Define table structure
product = []
volume_per_unit = []
cost_per_unit = []
units = []
cost = []

# Load data from JSON file and append data to table
with open('Python-main\CostPerVolume\data.json', 'r') as f:
    data = json.load(f)
    for item in data['description']:    
        product.append(item['product'])
        volume_per_unit.append(item['volume_per_unit'])
        cost_per_unit.append(item['cost_per_unit'])

# Use data from JSON file to calculate total units and total cost using calculated volume 
for i, c in enumerate(volume_per_unit):
    units.append(math.ceil(v / c))
for i, c in enumerate(cost_per_unit):
    cost.append(c * units[i])


table = zip(product, volume_per_unit, cost_per_unit, units, cost) 
with open('Python-main\Practice\Int\cost_per_sqaure.txt', 'w') as f:
    f.write(tabulate(table, headers=['Manufacturer', 'Product', 'Type', 'Area Per Unit', 'Cost Per Unit', 'Total Units', 'Total Cost'], tablefmt='github', numalign='left', floatfmt=".2f"))
   