# Match lines that are more than 30 characters long.
import re
sample = """
This line is way too loooooooooooong.
This one is fine.
This one is fine too.
This line is also too long................
"""
search = re.findall(r'\b.{30,}', sample)
print(search)