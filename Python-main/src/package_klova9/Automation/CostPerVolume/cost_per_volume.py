# Calculate cubic area of a toroid
# Determine units of material required to build toroid
# Determine cost of material required to build toroid
import json
import math
from tabulate import tabulate

x = 4.375 # Diameter of inner circle (ft)
y = 13.75 # Diameter of outer circle (ft)
z = 0.5 # Height of cylinder (ft)

# Volume of outer cylinder
v1 = math.pi * math.pow(y/2, 2) * z
# Volume of inner cylinder
v2 = math.pi * math.pow(x/2, 2) * z
# Volume of toroid
v = v1 - v2
print(math.ceil(v))

# Define table structure
manufacturer = []
product = []
volume_per_unit = []
cost_per_unit = []
units = []
cost = []

# Load data from JSON file and append data to table
with open('D:\Python\Python-main\src\package_klova9\Automation\CostPerVolume\data.json', 'r') as f:
    data = json.load(f)
    for item in data['manufacterure']:    
        manufacturer.append(item['name'])
        product.append(item['product'])
        volume_per_unit.append(item['volume_per_unit'])
        cost_per_unit.append(item['cost_per_unit'])

# Use data from JSON file to calculate total units and total cost using calculated volume 
for i, c in enumerate(volume_per_unit):
    units.append(math.ceil(v / c))
for i, c in enumerate(cost_per_unit):
    cost.append(c * units[i])

# Construct table with calculated data and write to text file
table = zip(manufacturer, product, volume_per_unit, cost_per_unit, units, cost) 
with open('\Python\Python-main\src\package_klova9\Automation\CostPerVolume\cost_per_volume.txt', 'w') as f:
    f.write(tabulate(table, headers=['Manufacturer', 'Product', 'Volume Per Unit', 'Cost Per Unit', 'Total Units', 'Total Cost'], tablefmt='github', numalign='left', floatfmt=".2f"))

print("File 'cost_per_volume.txt' has been created")