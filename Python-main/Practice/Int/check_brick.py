import math
# This code calculates the square footage of a certain number of bricks, given their dimensions and quantity, and also calculates the area of a circle with a specific inner and outer radius. It uses the math module to calculate the circle area and prints the results of both calculations.

brick_length = 8/12
brick_width = 4/12
brick_count = 9*35
brick_area = brick_count * (brick_length * brick_width)
square_feet = brick_area
inner_radius = 3.375
radius_1 = ((1 + inner_radius) / 2) ** 2
radius_2 = ((7 + inner_radius)/ 2) ** 2
circle_area = math.floor(math.pi * (radius_2 - radius_1))

print(f'Square feet of brick: {square_feet}')
print(f'Circle area: {circle_area}')
