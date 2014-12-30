"""Data Structures and Sequences"""

# tuple -------------------------------------------------------------------
tup = 4, 5, 6
tup
nested_tup = (4, 5, 6), (7, 8) # easy way to make tuples
nested_tup
nested_tup[0]
tuple([4, 0, 2])
tup = tuple('string')
tup
tup[0]
tup = tuple(['foo', [1, 2], True])
tup[2]
tup[1].append(3)
tup
(4, None, 'foo') + (6, 0) + ('bar',)
('foo', 'bar') * 4 # multiply list by number expands it


# unpacking tuples ---------------------------------------------------------

# python will try to unpack and match tuples
tup = (4, 5, 6)
a, b, c = tup
b
tup = 4, 5, (6, 7)
a, b, (c, d) = tup
d

# this makes swapping variables easy
tmp = a
a = b
b = tmp
# versus
b, a = a, b

# can unpack and iterate over a sequence
seq = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
for a, b, c in seq:
    pass


# tuple methods
# TUPLES CANNOT BE MODIFIED
# CREATED using "()"
a = (1, 2, 2, 2, 3, 4, 2)
a.count(2) # you can count values in tuples and lists
a.count(3)



# lists -----------------------------------------------------------------------
# CAN be modified
# created using "[]"
a_list = [2, 3, 7, None]
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list[1] = 'peekaboo'

# adding and removing elements
b_list.append('dwarf') # add to the end
b_list
b_list.insert(1, 'red') # insert in a particular spot
b_list
b_list.pop(2) # removes an element and returns it
b_list
b_list.append('foo')
b_list.remove('foo')
b_list
'dwarf' in b_list


# concatenating and combining lists -------------------------------------------
[4, None, 'foo'] + [7, 8 , (2, 3)]
x = [4, None, 'foo']
x.extend([7, 8, (2, 3)])
x

"""
## extend() is fast
everything = []
for chunk in list_of_lists:
    everything.extend(chunk)

## faster than concatenating with `+`
everything = []
for chunk in list_of_lists:
    everything = everything + chunk
"""

## sort
a = [7, 2, 5, 1, 3]
a.sort()
a
b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key = len) # sort by key type
b

## binary search and maintaining a sorted list
# bisect() finds where to place a value to keep a list sorted
# insort() actually puts a value there
import bisect
c = [1, 2, 2, 2, 3, 4, 7]
bisect.bisect(c, 2)
bisect.bisect(c, 5)
bisect.insort(c, 6)
c

## slicing
seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[1:5]
seq[3:4] = [6, 3]
seq[:5] # start indexing can be subbed with `:`
seq[3:] # same with stops
seq[-4:] # negative slicing
seq[2::] # an extra `:` can be used to create skips. here there are 2.
seq[::-1] # this reverses the vector


# BUILT-IN SEQUENCE FUNCTION ------------------------------------------------------
# enumerate
i = 0
some_list = ['foo', 'bar', 'baz']
mapping = dict((v, i) for i, v in enumerate(some_list))

for value in some_list:
    # do something to enumerate
    i += 1

for i, value in enumerate(some_list):
    # do something with value
    print(value)


# sorted
sorted([7, 1, 2, 6, 0, 3, 2])
sorted('horse race')
sorted(set('this is just some string')) # `set` gets all unique values



# zip -------------------------------------------------------------------------
seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zip(seq1, seq2) # creates like (x,y) pairs etc.
seq3 = [False, True]
zip(seq1, seq2, seq3)

for i, (a, b) in enumerate(zip(seq1, seq2)):
    print('%d: %s, %s' % (i, a, b))

pitchers = [('Nolan', 'Ryan'), ('Roger', 'Clemens'), ('Schilling', 'Curt')]
first_names, last_names = zip(*pitchers)
first_names
last_names
zip(*pitchers)  # `*` is a function call.
                # same as zip(pitchers[0], ..., pitchers[len(pitchers) - 1])
# reversing values
list(range(10))
list(reversed(range(10)))



# dict -----------------------------------------------------------------------
## creating dictionaries, adding key-values, removing values etc.
empty_dict = {} # key-value pairs
d1 = {'a' : 'some value', 'b' : [1, 2, 3, 4]}
d1[7] = 'an integer' # elements can also be keys
'b' in d1
d1[5] = 'some value'
d1['dummy'] = 'another value'
del d1[5] # remove via key
d1
ret = d1.pop('dummy') # yanks a value. removes it from d1 but saves as ret.
ret
d1.keys()
d1.values()
d1.update({'b' : 'foo', 'c' : 12}) # merges
d1

## creating dicts from sequences
# using for loops
mapping = {}
key_list = ('a', 'b', 'c')
value_list = ([1, 2, 3, 4], [5, 6, 7], ['a', 'b', 'c'])

for key, value in zip(key_list, value_list):
    mapping[key] = value

mapping

# using zip -- much faster
mapping1 = dict(zip(key_list, value_list))
mapping
mapping1

## default values
# standard to do if-else to look for a key in a list. if not here, return default
some_dict = dict(zip(key_list, value_list))
default_value = 5

if key in some_dict:
    value = some_dict[key]
else:
    value = default_value

# this can be done in one line!
some_dict = dict(zip(key_list, value_list))
value = some_dict.get('a', default_value)   # if `get` doesn't pull a key, returns
                                            #   None. `pop` fails, returns none.

# other lists can also be defaults
# here, we categorize list by first letters
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
    letter = word[0]
    if letter not in by_letter:
        by_letter[letter] = [word]
    else:
        by_letter[letter].append(word)


words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

# you can compress the if-else into a single line
for word in words:
    letter = word[0] # get the first letter
    by_letter.setdefault(letter, []).append(word) # compressed

by_letter


# even easier using collections
from collections import defaultdict
by_letter = defaultdict(list)
for word in words:
    by_letter[word[0]].append(word)

counts = defaultdict(lambda: 4)


# valid dict key types
# keys must be immutable scalar types: int, float, string or tuples
# the technical term is "hashable"
hash('string')
hash((1, 2, (2, 3)))
hash((1, 2, [2, 3])) # fails cause [2, 3] is a list. list are mutable.

# can use a list if we convert it to a tuple
d = {}
d[tuple([1, 2, 3])] = 5
d


# SET ----------------------------------------------------------
# sets are like dicts but keys only, no values
set([2, 2, 2, 1, 3, 3])
set([1, 2, 3])

{2, 2, 2, 1, 3, 3}
set([1, 2, 3])

# set operations
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
a | b # union (or)
set(range(1,8))
a & b # instersection (and)
a - b # difference
set([1, 2, 6, 7, 8])
a_set = {1, 2, 3, 4, 5}
{1, 2, 3}.issubset(a_set) # can check if something is a subset
a_set.issuperset({1, 2, 3}) # and also a superset
{1, 2, 3} == {3, 2, 1}

# python set operations
a = set(range(7))
b = set(range(5, 11))
x = 8
a.add(x) # add element x to the set a
a.remove(x) # remove element x from set a
a.union(b) # a | b
a.intersection(b) # a & b
a.difference(b) # a - b
a.symmetric_difference(b) # a ^ b (a or b but not both)
a.issubset(b)
a.issuperset(b)
a.isdisjoint(b)



# LIST, SET, AND DICT COMPREHENSION -------------------------------
"""
list comprehension are one of the most-loved python language feature.
 allows you to concisely form a new list by filtering the elements of
 a collection and transforming the elements passing the filter in one
 conscise experession. they take the basic form:

    [expr for val in collection if condition]

This is equivalent to the following for loop:

    result = []
    for val in collection:
        if condition:
            result.append(expr)
"""
# filter out strings len() > 2 and converts to uppercase
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']
[x.upper() for x in strings if len(x) > 2]

"""
A dict comprehension looks like this:

    dict_comp = {key-expr : value-expr for value in collection
                    if condition}

A set comprehension looks like the equivalent list comprehension except with curly
braces instead of square brackets:

    set_comp = {expr for value in collection if condition}
"""
# set comp example
unique_lengths = {len(x) for x in strings}
unique_lengths

# dict comp example
loc_mapping = {val : index for index, val in enumerate(strings)}
loc_mapping # set with keys aka set-value

# equivalent to...
loc_mapping = dict((val, idx) for idx, val in enumerate(strings))
loc_mapping

# NESTED LIST COMPREHENSIONS -----------------------------------------------
# take a list of lists
all_data = [['Tom', 'Billy', 'Jefferson', 'Andrew', 'Wesley', 'Steven', 'Joe'],
    ['Susie', 'Casey', 'Jill', 'Ana', 'Eva', 'Jennifer', 'Stephanie']]

# suppose we wanted a single list containing all names with two or more e's in them

# this for loop can be condensed...
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.extend(enough_es)

#...into one line!
result = [name for names in all_data
                for name in names if name.count('e') >= 2]

# another example, in one line
some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for tup in some_tuples for x in tup]
flattened

# here as a nested loop
flattened = []
for tup in some_tuples:
    for x in tup:
        flattened.append(x)

# can make a list within lists
[[x for x in tup] for tup in some_tuples]

