# Count the number of months between two dates
# Input: two dates in the format 'MM-DD-YYYY'

from datetime import datetime

date1 = input('Enter the first date in the format YYYY-MM-DD: ')
date2 = input('Enter the second date in the format YYYY-MM-DD:: ')

def count_months(date1, date2):
    date1 = datetime.strptime(date1, '%Y-%m-%d')
    date2 = datetime.strptime(date2, '%Y-%m-%d')
    return abs((date1.year - date2.year) * 12 + date1.month - date2.month)

print(f'The number of months between the two dates is: {count_months(date1, date2)}')
