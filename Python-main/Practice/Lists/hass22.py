#Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(arr):
    for index, values in enumerate(arr):
        if values == 2 and arr[index-1] == 2:
            return True
    return False
      
print(has22([1, 2, 2]))# → True
print(has22([1, 2, 1, 2]))# → False*
print(has22([2, 1, 2]))# → False