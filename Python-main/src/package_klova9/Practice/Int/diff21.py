"""
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
"""
def difference(n):
    if n <= 21:
        print(21 - abs(n))
    elif n > 21:
        print((21 - abs(n))*2)
    else:
        print("Enter a valid number")
        
difference(2)
difference(-10)
difference(22)
