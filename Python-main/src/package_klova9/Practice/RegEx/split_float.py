# Leave only two numbers after the floating point in every number
import re 
sample = """
1 Euro = 1.351299 US Dollar
British Pound = 1.614873 US Dollar
Australian Dollar = 0.916063 US Dollar
Canadian Dollar = 0.947400 US Dollar
Emirati Dirham = 0.272257 US Dollar
Swiss Franc = 1.096267 US Dollar
Chinese Yuan = 0.164114 US Dollar
Malaysian Ringgit = 0.310681 US Dollar
New Zealand Dollar = 0.819950 US Dollar
"""
search = re.sub(r'(\d\.\d\d)\d*', r'\1', sample)
print(search)