# Match numbers containing floating point. Skip those that don't.
import re
sample = """Speed of light in vacuum 299792458 m/s Standard atmosphere 101325 Pa Earth to sun distance 149600000 km Acceleration of gravity 9.80665 m/s^2 Circumference to diameter ratio 3.141592 Gas constant 8.3144621 J/mol*K"""
search = re.findall(r'\d+\.\d+', sample)
print(search)