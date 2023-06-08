#Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array

def big_diff(numbers):
    numbers.sort()
    print(f'{numbers[0]} is min, {numbers[-1]} is max')
    print(f'Difference of {numbers[-1] - numbers[0]}')
    

big_diff([10, 3, 5, 6])# → 7
big_diff([7, 2, 10, 9])# → 8
big_diff([2, 10, 7, 2])# → 8