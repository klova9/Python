#Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

def lone_sum(a, b, c):
    sum = 0
    if a == b:
        sum = c
    if a == c:
        sum = b
    if b == c:
        sum = a
    if a == c and a == b:
        sum = 0
    else:
        sum = a + b + c
    print(sum)

lone_sum(1, 2, 3)# → 6
lone_sum(3, 2, 3)# → 2
lone_sum(3, 3, 3)# → 0