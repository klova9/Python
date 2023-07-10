"""
Given a string and a non-negative int n, return a larger string that is n copies of the original string.
"""

def string_times(n, str):
    i = 1
    while i <= n:
        print(str, end="")
        i+=1
    print()
string_times(2, "String")
string_times(1, "Hi")
string_times(5, "GoodMorning")
