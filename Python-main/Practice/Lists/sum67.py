#Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.

def sum67(arr):
    sum = 0
    negate = False
    for i in arr:
        if i ==6:
            negate = True
            continue
        if i == 7 and negate:
            negate = False
            continue
        if negate == False:
            sum += i
    print(sum)       

sum67([1, 2, 2])# → 5
sum67([1, 2, 2, 6, 99, 99, 7])# → 5
sum67([1, 1, 6, 7, 2])# → 4