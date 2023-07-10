# Some words in this text are accidentally repeated. Remove the doubles.
import re
sample = """
It was a chilly November afternoon. I had just just consummated an unusually hearty dinner, of which the dyspeptic truffe formed not the least important item, and was sitting alone in the dining-room dining-room, with my feet upon the the fender, and at my elbow a small table which I had rolled up to the fire, and upon which were some apologies for dessert, with some miscellaneous bottles bottles of wine, spirit and liqueur. In the morning I had had been reading Glover's "Leonidas", Wilkie's Wilkie's "Epigoniad", Lamartine's "Pilgrimage", Barlow's "Columbiad", Tuckermann's "Sicily", and Griswold's "Curiosities" ; I am willing to confess, therefore, that I now felt a little stupid.
"""
search = re.sub(r'(\b\w+\b)\W+\1', r'\1', sample)
print(search)