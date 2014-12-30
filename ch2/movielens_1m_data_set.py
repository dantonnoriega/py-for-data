"""MovieLens 1M Data Set"""
from __future__ import print_function, division
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

mainDir = "/Users/dnoriega/GitHub/pyfordata/ch2/"

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(mainDir + 'ml-1m/users.dat', sep='::', header=None,
    names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(mainDir + 'ml-1m/ratings.dat', sep='::', header=None,
    names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table(mainDir + 'ml-1m/movies.dat', sep='::', header=None,
    names=mnames)

## see the first 5 rows
users[:5]
ratings[:5]
movies[:5]
ratings

## merging data
data = pd.merge(pd.merge(ratings, users), movies)
data

## finding means using `pivot_table`. can group by `gender`.
## `pivot_table` produces another DataFrame.
mean_ratings = data.pivot_table('rating', rows='title', cols='gender',
    aggfunc='mean')
mean_ratings[:5]
type(mean_ratings)

## can group data and get a Series of group sizes using `.groupby` and `.size`
ratings_by_title = data.groupby('title').size()
ratings_by_title[:10]

## we can get the index of where this is true using `.index`
active_titles = ratings_by_title.index[ratings_by_title >= 250]
active_titles

## can extract info using index vector via `.ix`
mean_ratings = mean_ratings.ix[active_titles]
mean_ratings

## see top female viewers. first sort by F column in descending
top_female_ratings = mean_ratings.sort_index(by='F', ascending=False)
top_female_ratings[:10]



# Measuring rating disagreement --------------------------------------
## create variable 'diff' then sort by that variable
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_index(by = 'diff')
sorted_by_diff[:15]

## quick look at indexing
sorted_by_diff # as is
sorted_by_diff[::1] # advance by ones
sorted_by_diff[::2] # advance by twos
sorted_by_diff[::-1] # same, reversed
sorted_by_diff[::-2]

## reverse order of rows, take first 15
# following are equivalent
sorted_by_diff[::-1][:15]
sorted_by_diff[::1][-15:].sort_index(by='diff', ascending=False)

## suppose instead you wanted the movies that elicited the most
##   disagreement among viewers (aka highest variance)

# standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()

# filter down to active_titles
rating_std_by_title = rating_std_by_title.ix[active_titles]

# order series by value in descending order
rating_std_by_title.order(ascending=False)[:10]

