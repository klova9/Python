#Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

def sum13(numbers):
    block = False
    sum = 0
    for x in range(len(numbers)):
        if numbers[x] == 13 or (numbers[x-1] == 13 and not numbers[:-1]):
            block = True
        if block == False:
            sum += numbers[x]
    print(sum)
sum13([1, 2, 2, 1])# → 6
sum13([1, 1])# → 2
sum13([1, 2, 2, 1, 13])# → 6