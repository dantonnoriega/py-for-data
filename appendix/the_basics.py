"""appendix: python intro, the basics"""

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

# use methods on datetime to extract data
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

