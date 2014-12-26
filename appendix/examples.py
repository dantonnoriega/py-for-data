"""appendix: python intro"""

## referencing ---------------------------------------------------
a = [1, 2, 3]
b = a # both `a` and `b` reference list [1,2,3]

a.append(4) # updating `a` really updates `[1,2,3]`, which affects b
b


## pass by reference ---------------------------------------------
def append_element(some_list, element):
	some_list.append(element)

a = [1, 2, 3]
append_element(a, 4) # python only passes references to functions. no copies made!
a


## strong types --------------------------------------------------
try:
    5 + '5' # fails and python does NOT convert (generally). hence, strong types.
except:
    pass

a = 4.5 ; b = 2
type(a) ; type(b)
a / b
type(a / b)

isinstance(a, int) # False. `a` is not integer
isinstance(a, float) # True
isinstance(a, (int, float)) # handles both


## attributes and methods -----------------------------------------
a = 'foo' # a.<Tab> will find them in IPython. in ST3, ctrl+space


## "Duck" typing --------------------------------------------------
def isiterable(obj): # checks if something is "iterable"
	try:
        iter(obj)
        return True
    except TypeError:
        return False


isiterable('a string') # True
isiterable(5) # False
isiterable([1, 2]) # True

x = "hey hi yo"

if not isinstance(x, list) and isiterable(x): # checks if not list and iterable
    x = list(x)
    print(x) # now its a list!


## imports ---------------------------------------------------------
cd /Users/dnoriega/GitHub/pyfordata/appendix

# save a file `some_module.py` for import
import some_module
result = some_module.f(5)
pi = some_module.PI
# ??some_module.g # we can look at the functions
# ??some_module.f # etc.

# equivalently
from some_module import f, g, PI
result = g(5, PI)

# by using `as` keywords, we can give imports different values
import some_module as sm
from some_module import PI as pi, g as gf

r1 = sm.f(pi) # some_module as `sm`
r2 = gf(6, pi) # PI as `pi`, g as `gf`


## binary operators and comparisons --------------------------------

5 > 7 # False
5 < 7 # True

# to check references, use `is` and `is not`
a = [1, 2, 3] # a with the list
b = a 	# b references a

c = list(a) # `list()` makes a new list
a is b # True. both reference the same list.
a is c # False. a and c reference different lists
a == c # True. `==` checks VALUE, not reference
a = None
a is None


## grant list of binary operators ----------------------------------
a = 4.0
b = 3.0

a + b 	# Add a and b
a - b 	# Subtract b from a
a * b 	# Multiply a by b
a / b 	# Divide a by b
a // b 	# Floor-divide a by b, dropping any fractional remainder
a ** b 	# Raise a to the b power
a & b 	# True if both a and b are True. For integers, take the bitwise AND.
a | b 	# True if either a or b is True. For integers, take the bitwise OR.
a ^ b 	# For booleans, True if a or b is True, but not both. For integers,
		# 	take the bitwise EXCLUSIVE-OR.
a == b 	# True if a equals b
a != b 	# True if a is not equal to b
a <= b, a < b 	# True if a is less than (less than or equal) to b
a > b, a >= b 	# True if a is greater than (greater than or equal) to b
a is b 			# True if a and b reference same Python object
a is not b 		# True if a and b reference different Python objects


## strictness vs laziness --------------------------------------------
# python uses strict evaluation
# strict evaluatation is immediate.
# lazy evaluation means value assigned if obj used
a = b = c = 5 # statements are immediately (or strictly) evaluated
d = a + b * c


## mutable and immutable objects -------------------------------------
a_list = ['foo', 2, [4, 5]]
type(a_list) # lists are mutable (you can change values)
a_list[2] = (3, 4)
a_list

a_tuple = (3, 5, (4, 5))
type(a_tuple) # tuples are immutable (cannot change value)
a_tuple[1] = 'four' # error


## scalar types -------------------------------------------------------

# types are: None, str, unicode, float, bool, int, long

# numeric types: int, floag, long
ival = 17239871
ival ** 3

fval = 7.234
fval2 = 6.78e-5 # sci notation allowed


# python 2.7 vs 3
5 / 3 # integers wont convert to float in python 2.7
from __future__ import division # this makes it so it does
5 / 3
5 // 3

cval = 1 + 2j
cval * (1 - 2j)

# strings
a = 'one way of writing a string'
b = 'another way'

# multiline strings
c = """
This is a longer string that
spans multiple lines
"""

# strings are immutable
a = 'this is a string'
a[10]
a[10] = 'f' # cant change immutable objects
b = a.replace('string', 'longer string') # create a new string using `.replace`
b

# converting types to string
a = 5.6 ; a
s = str(a) ; s

# strings are a seq of characters
s = 'python'
list(s)
s[:3]

# escape characters
s = '12\\34'
print s

# using leading `r` to reinterpret
s = r'this\has\no\special\charcters'
s

# concat
a = 'this is the first half'
b = 'and this is the second half'
a + b

# inserting values
template = '%.2f %s are worth $%d'
template % (4.556, 'Argentine Pesos', 1)

# booleans
True and True
False and True
a = [1, 2, 3]
if a:
	print 'I found something!'

b = []
if not b:
	print 'Empty!'

bool([]), bool([1, 2, 3])
bool('Hello world!'), bool('')
bool(0), bool(1)

# type casting -----------------------------------------------------
s = '3.14159'
fval = float(s)
type(fval)
int(fval)
bool(fval)
bool(0)

# None -------------------------------------------------------------
a = None
a is None
b = 5
b is not None

def add_and_maybe_multiply(a, b, c = None):
	result = a + b
	if c is not None:
		result = result * c
	return result

# DATE AND TIME ----------------------------------------------------
from datetime import datetime, date, time

dt = datetime(2011, 10, 29, 20, 30, 21) # dt is not a datetime obj

# use methods on datetime to extract methods
dt.day
dt.minute
dt.date()
dt.time()
dt.strftime('%m/%d/%Y %H:%M') # make string of time
datetime.strptime('20091031', '%Y%m%d') # strip time
dt.replace(minute = 0, second = 0)

dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt
delta
dt + delta # = dt2


# control flow -----------------------------------------------------
x = 2

if x < 0:
	print "It's negative"

# `if`, `elif` controls flow, `else` is a catch all
if x < 0:
	print "It's negative"
elif x == 0:
	print 'Equal to zero'
elif 0 < x < 5:
	print 'Postive but smaller than 5'
else:
	print 'Postive and larger than or equal to 5'

a = 5; b = 7
c = 8; d = 4

if a < b or c > d:
	print 'Made it'


# for loops --------------------------------------------------------

collection = [a, b, c, d]
for value in collection:
	print value

sequence = [1, 2, None, 4, None, 5]
total = 0
for value in sequence:
	if value is None:
		continue
	total += value

total # started at 0 now 12

sequence = [1, 2, 0, 4, 6, 5, 2, 1]
total_until_5 = 0

for value in sequence:
	total_until_5 += value
	if value == 5:
		break


# while loops --------------------------------------------------------
x = 256
total = 0
while x > 0:
	if total > 500:
		break
	total += x
	x = x // 2

x


# pass ----------------------------------------------------------------

# pass is used a sort of placeholder while working on code in python
x = 3
if x < 0:
	print 'negative!'
elif x == 0:
	# TODO: put something smart here
	pass # used to nullify blocks. only required since python takes whitespace
else:
	print 'positive!'

def f(x, y, z):
	# TODO: implement this function!
	pass


# exception handling ---------------------------------------------------
float('1.2345')
float('something')

def attempt_float(x):
	try:
		return float(x)
	except:
		return x

attempt_float('1.2345')
attempt_float('something')
float((1,2))

def attempt_float(x):
	try:
		return float(x)
	except ValueError:
		return x

attempt_float('1.2345')
attempt_float('something')
attempt_float((1,2))

def attempt_float(x):
	try:
		return float(x)
	except (TypeError, ValueError):
		return x

# range and xrange -------------------------------------------------------
range(10)
range(0, 20, 2)
seq = [1, 2, 3, 4]
for i in range(len(seq)):
	val = seq[i]

sum = 0
for i in xrange(10000):
	# % is the modulo operator
	if x % 3 == 0 or x % 5 == 0:
		sum += i


# ternary expressions ----------------------------------------------------

# a "ternary expression" combines if-else blocks to produce a value
#	e.g. value = true-expr if condition else false-expr

# in one line
value = 8 if x < 3 else 9

# in a block
if x < 3:
	value = 8
else:
	value = 9

x = 5
'Non-negative' if x >= 0 else 'Negative'


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
## extend() is fast
everything = []
for chunk in list_of_lists:
	everything.extend(chunk)

## faster than concatenating with `+`
everything = []
for chunk in list_of_lists:
	everything = everything + chunk

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
zip(*pitchers) 	# `*` is a function call.
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
value = some_dict.get('a', default_value) 	# if `get` doesn't pull a key, returns
											#	None. `pop` fails, returns none.

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
    enough_es = [name for name in names if name.count('e') > 2]
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


# FUNCTIONS ----------------------------------------------------------
def my_function(x, y, z = 1.5):
    if z > 1:
        return z * (x + y)
    else:
        return z / (x + y)

# "positional" arguments vs "keyword" arguments
"""keyword = commonly used to specify default values or optional args.
`my_function` can be called in the following two ways"""

my_function(5, 6, z = 0.7)
my_function(3.14, 7, 3.5)

"""main restriction: keyword arguments MUST follow the positional
 arguments (if any). keyword arguments can be in any order."""


## NAMESPACES, SCOPE, AND LOCAL FUNCTIONS ---------------------------
# global vs local scopes
# within functions = local (think R)

# compare...
def func():
    a = []
    for i in range(5):
        a.append(i)

func()
a # list is empty since a is not passed outside the func

# ... to
a = []
def func():
    for i in range(5):
        a.append(i)

func()
a # not empty -- `a` reference was updated

## assigning global values within functions is possible using `global`
a = None

def bind_a_variable():
    global a
    a = []

bind_a_variable()
print a # its `[]` not `None`

"""Functions can be declared anywhere, and there is no problem with having local functions
that are dynamically created when a function is called:

    def outer_function(x, y, z):
        def inner_function(a, b, c):
            pass
        pass

In the above code, the inner_function will not exist until outer_function is called. As
soon as outer_function is done executing, the inner_function is destroyed."""


# RETURNING MULTIPLE VALUES ------------------------------------------
## awesome feature! return multiple values
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c

a, b, c = f()
a, b, c


# FUNCTIONS ARE OBJECTS ----------------------------------------------
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
'south carolina##', 'West virginia?']

## Using functions for cleaning data
import re # regular expression module

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip() # remove whitespace
        value = re.sub('[!#?]', '', value) # remove punctuation
        value = value.title() # cap first word (Title)
        result.append(value)
    return result

clean_strings(states)


## remove certain values
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
'south carolina##', 'West virginia?']

def remove_punctuation(value):
    return re.sub('[!%?]', '', value)

clean_ops = [str.strip, remove_punctuation, str.title] # create fun list

def clean_strings(strings, ops):
    result = []
    for value in strings:
        for function in ops:
            value = function(value) # here we take functions and apply them
        result.append(value)
    return result

clean_strings(states, clean_ops) # much more concise

## `map(function, sequence)` applies functions to values
states = [' Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda',
'south carolina##', 'West virginia?']


# ANONYMOUS (lambda) FUNCTIONS -----------------------------------
## following are the same
def short_function(x):
    return x * 2

equiv_anon = lambda x: x * 2

## creating neat, reusable functions
def apply_to_list(some_list, f):
    return [f(x) for x in some_list]

ints = [4, 0, 1, 5, 6]
apply_to_list(ints, lambda x: x * 2)

# more succinct but the same as
[x * 2 for x in ints]

## another example
# sort strings by the number of distinct letters
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
strings.sort(key = lambda x: len(set(list(x))))
strings


#  CLOSURES: FUNCTIONS THAT RETURN FUNCTIONS -----------------------
def make_closure(a):
    def closure():
        print 'I know the secret: %d' % a
    return closure

closure = make_closure(5)
closure()

# here is a function that returns a function that keeps
#   track of the arugments it has been called with:

def make_watcher():
    have_seen = {}

    def has_been_seen(x):
        if x in have_seen:
            return True
        else:
            have_seen[x] = True
            return False
    return has_been_seen

watcher = make_watcher()
vals = [5, 6, 1, 5, 1, 6, 3, 5]
[watcher(x) for x in vals]


## since you cannot bind values in functions, one can instead
## use functions to update lists or dicts
def make_counter():
    count = [0]
    def counter():
        count[0] += 1
        return count[0]
    return counter # `counter` references list `count`

counter = make_counter() # here, we modify the object `counter`
counter() # 1
counter() # 2
counter() # 3

# another example, formatting to string
def format_and_pad(template, space):
    def formatter(x):
        return (template % x).rjust(space)
    return formatter

fmt = format_and_pad('%.4f', 15) # initialize function
fmt(1.756)



# Extended Call Syntax with *args, **kwargs -----------------------
"""
When you write func(a, b, c, d=some, e=value), the positional and keyword
arguments are actually packed up into a tuple and dict, respectively. So the internal
function receives a tuple args and dict kwargs and internally does the equivalent of:

    a, b, c = args
    d = kwargs.get('d', d_default_value)
    e = kwargs.get('e', e_default_value)
"""

## to see whats happening...
def say_hello_then_call_f(f, *args, **kwargs):
    print 'args is', args
    print 'kwargs is', kwargs
    print("Hello! Now I'm going to call %s" % f)
    return f(*args, **kwargs)

def g(x, y, z=1):
    return (x + y) / z

say_hello_then_call_f(g, 1, 2, z = 5.)

