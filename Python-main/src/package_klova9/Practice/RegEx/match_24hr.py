# Match valid time in 24h format
import re
sample = """
Valid and invalid time:
00:15
07:40
08:61
09:59
13:00
14:7
20:20
23:61
24:15
"""
search = re.findall(r'(?:[01][0-9]|2[0-3])[:][0-5][0-9]', sample)
print(search)