# Change date formats from yyyy-mm-dd to dd.mm.yyyy
import re
sample = """
Robert Boyle 1627-01-25 — 1691-12-31
Antoine Lavoisier 1743-08-26 — 1794-05-08
Michael Faraday 1791-09-22 — 1867-06-25
Louis Pasteur 1822-12-27 — 1895-09-28
Alfred Nobel 1833-10-21 — 1896-12-10
Dmitri Mendeleev 1834-02-08 — 1907-02-02
Marie Curie 1867-11-07 — 1934-07-04
Linus Pauling 1901-02-28 — 1994-08-19
"""
search = re.sub(r'(\d{4})-(\d{2})-(\d{2})',r'\3.\2.\1', sample)
print(search)