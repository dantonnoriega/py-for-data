"""Functions"""

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


# Currying: Partial Argument Application ----------------------------
"""
Currying is a fun computer science term which means deriving new functions from
existing ones by partial argument application. For example, suppose we had a trivial
function that adds two numbers together:
"""

def add_numbers(x, y):
    return x + y

"""
Using this function, we could derive a new function of one variable, add_five, that adds
5 to its argument:
"""
add_five = lambda y: add_numbers(5, y)

"""
The second argument to add_numbers is said to be curried.
"""


# Generators ---------------------------------------------------------
# iterating over dict gives keys
some_dict = {'a': 1, 'b': 2, 'c': 3}
for key in some_dict:
    print key,

dict_iterator = iter(some_dict) # creates iterator for loops

# generators create new iterable objects, returning lists/seq,
#   not single vals.
# create generators using `yield` instead of `return`
def squares(n=10):
    print 'Generating squares from 1 to %d' % (n ** 2)
    for i in xrange(1, n + 1):
        yield i ** 2

# when calling gens, they are not executed immediately only
#   once request for iterating
gen = squares()
gen

for x in gen:
    print x,

# example, making change:
def make_change(amount, coins=[1, 5, 10, 25], hand=None):
    hand = [] if hand is None else hand
    if amount == 0:
        yield hand
    for coin in coins:
        # ensures we don't give too much change, and combinations are unique
        if coin > amount or (len(hand) > 0 and hand[-1] < coin):
            continue
        for result in make_change(amount - coin, coins=coins,
                            hand=hand + [coin]):
            yield result

for way in make_change(100, coins = [10, 25, 50]):
    print way

len(list(make_change(100)))


# Generator expressions ---------------------------------------------
# similar to list, dict, and set comprehension
gen = (x ** 2 for x in xrange(100)) # use () not []

# same as
def _make_gen():
    for x in xrange(100):
        yield x ** 2

gen = _make_gen()

# can be used inside any python function that accepts generators
sum((x ** 2 for x in xrange(100)))
dict((i, i ** 2) for i in xrange(5))



# itertools module --------------------------------------------------
import itertools

# example, `groupby` takes seqs and funcs and groups by return val
first_letter = lambda x: x[0]
names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, names in itertools.groupby(names, first_letter):
    print letter, list(names) # `names` is a generator

# list of useful itertools functions
"""
# Generator version of the built-in map; applies func to each zipped tuple of
the passed sequences.

    imap(func, *iterables)

# Generator version of the built-in filter; yields elements x for which
func(x) is True.

    ifilter(func, iterable)

# Generates a sequence of all possible k-tuples of elements in the iterable,
ignoring order.

    combinations(iterable, k)

# Generates a sequence of all possible k-tuples of elements in the iterable,
respecting order.

    permutations(iterable, k)

# Generates (key, sub-iterator) for each unique key

    groupby(iterable[, keyfunc])
"""



