import re
# Open file as fl1
with open(r'Automation\visit_list.txt', 'r+') as fl1:
    data = fl1.read()
# Create new file "txt_fixed.txt"
    txt_fixed = open('txt_fixed.txt', 'w+')
# Sperate words by capital
    txt_fixed.write(re.sub(r'([A-Z])', r' \1', data))
