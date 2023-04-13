"""
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
"""
def near_hundred(n):
    if abs(100 - abs(n)) <= 10 or abs(200 - abs(n)) <= 10:
        print("True")
    else:
        print("False")
        
near_hundred(93)
near_hundred(-90)
near_hundred(73)
