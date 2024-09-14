import math

# Define floor dimensions
lengh = 26
width = 13
area = lengh * width

# Define unit area and cost
unit_area = 2
unit_cost = 1.99

total_units = math.ceil(area / unit_area)
total_cost = total_units * unit_cost

print(f'{total_units} units, ${total_cost}')

