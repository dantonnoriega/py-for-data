"""Introductory Examples"""
from __future__ import print_function, division
import pylab
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## enable interact
# 1.usa.gov data from bit.ly -----------------------------------------
path = '/Users/dnoriega/GitHub/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()

import json
path = '/Users/dnoriega/GitHub/pydata-book/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]
records[0]
records[0]['tz']
print(records[0]['tz'])

# Counting Time Zones in Pure Python ---------------------------------
try:
    time_zones = [rec['tz'] for rec in records] # causes error
except:
    pass

# turns out that not all records have a time zone field
# easy to handle if we add `if 'tz' in rec`
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
time_zones[:10]


def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
            counts[x] += 1
        else:
            counts[x] = 1
    return counts

# or
from collections import defaultdict

def get_counts2(sequence):
    counts = defaultdict(int) # values will initialize to 0
    for x in sequence:
        counts[x] += 1
    return counts

# results in
counts = get_counts(time_zones)
counts
counts['America/New_York']
len(time_zones)

counts = get_counts2(time_zones)
counts

# top 10 time zones and counts
def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:] # reverse from pg. 411

top_counts(counts)

# using pandas
from pandas import DataFrame, Series
import pandas as pd
frame = DataFrame(records)
frame

tz_counts = frame['tz'].value_counts()
tz_counts[:10]
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = "Unkown"
tz_counts = clean_tz.value_counts()
tz_counts[:10]

# plots
tz_counts[:10].plot(kind='barh', rot = 0)
frame['a'][1]
frame['a'][50]
frame['a'][51]
results = Series([x.split()[0] for x in frame.a.dropna()])
results[:5]
results.value_counts()[:8]
plt.show() # need this to see plots!

# decompose top time zones into windows and non-windows
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),
    'Windows', 'Not Windows')
operating_system[:5]

# then group the data by its time zone column and this new list of OSs
by_tz_os = cframe.groupby(['tz', operating_system])

# the group counts, analogous to `value_counts` function above, can
#   be computed using `size`. the result is then reshaped into
#   a table with `unstack`.
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:10]

# select the top overall time zones. to do so, i construct an indirect
#   index array from the row counts in `agg_counts`:
indexer = agg_counts.sum(1).argsort()
indexer[:10]

# use `take` to select the rows in that order, then slice off last 10 rows
count_subset = agg_counts.take(indexer)[-10:]
count_subset

# this data can be plotted as a bar graph
count_subset.plot(kind='barh', stacked = True)
plt.show() # need this to see plots!

# normalized
normed_subset = count_subset.div(count_subset.sum(1), axis = 0)
normed_subset.plot(kind = 'barh', stacked = True)
plt.show() # need this to see plots!


