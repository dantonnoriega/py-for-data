### appendix: python intro

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
	'5' + 5 # fails and python does NOT convert (generally). hence, strong types.
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
	x = list(x) ; print(x) # now its a list!


## imports ---------------------------------------------------------
cd /Users/dnoriega/GitHub/pyfordata/appendix

# save a file `some_module.py` for import
import some_module
result = some_module.f(5)
pi = some_module.PI
??some_module.g # we can look at the functions
??some_module.f # etc.

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
a_tuple[1] = 'four'


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

# strings are immutable?
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
dt + delta


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
if value == 5:
break
total_until_5 += value


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
some_dict = zip(key_list, value_list)
default_value = 5
if key in some_dict:
	value = some_dict[key]
else:
	value = default_value

# this can be done in one line!
value = some_dict.get(key, default_value) 	# if `get` doesn't pull a key, returns
											#	None. `pop` fails, returns none.

# other lists can also be defaults
# here, we categorize list by first letters
words = ['apple', 'bat', 'bar', 'atom', 'book']
by_letter = {}

for word in words:
	letter = word[0] # get the first letter
	if letter not in by_letter: # see if first letter exists as key
		by_letter[letter] = [word] # if it doesn't, make it a key and assign value
	else:
		by_letter[letter].append(word) # else, append word to key by letter

by_letter

# you can compress the if-else into a single line
for word in words:
	letter = word[0] # get the first letter
	by_letter.setdefault(letter).append(word) # compressed

by_letter

