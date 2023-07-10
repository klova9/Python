# In this excercise you need to match 12 and 24 bit colors whose red, green and blue components are equal. Colors start with a '#'.

import re
sample = """
AliceBlue #F0F8FF
AntiqueWhite #FAEBD7
Aqua #00FFFF
Aquamarine #7FFFD4
Azure #F0FFFF
12 bit:
White #FFF
Red #F00
Green #0F0
Blue #00F
"""
search = re.findall('.*\b\#(\d)\1+\b', sample)
print(search)