#Return the number of even ints in the #
#given array. Note: the % "mod" operator #computes the remainder, e.g. 5 % 2 is 1.

def count_evens(numbers):
    count = 0
    for x in numbers:
        if x % 2 == 0:
             count += 1
    print(count)
count_evens([2, 1, 2, 3, 4])# → 3
count_evens([2, 2, 0])# → 3
count_evens([1, 3, 5])# → 0