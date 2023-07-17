# Match 24-bit hexadecimal colors. Skip 12 bit colors.

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
search = re.findall(r'.*\#.{3}', sample)
print(search)