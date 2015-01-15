"""
US Baby Names 1880-2010
"""

import os
import pandas as pd

path = '/Users/dnoriega/GitHub/pyfordata/ch2'
os.chdir(path)

# sample code for importing one file. inefficient.
names1880 = pd.read_csv('names/yob1880.txt',
    names = ['name', 'sex', 'births'])

names1880
names1880.head(10)

names1880.groupby('sex').births.sum()

# 2010 is the last available year right now
years = range(1880, 2011)

pieces = []

columns = ['name', 'sex', 'births']

for year in years:
    path = 'names/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)

    frame['year'] = year
    pieces.append(frame)


# Concatenate everything into a single DataFrame
names = pd.concat(pieces, ignore_index=True)
