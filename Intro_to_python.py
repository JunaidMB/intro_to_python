''' 
Introduction to Basic Python Ideas

Main ideas taken from Python for Data Analysis by Wes Mckinney - READ THE RELEVANT CHAPTERS

'''

# Variable Assignment
a = 5
b = 'cookie'
c = 10

d = a
print(d)

a == c
#a is c

# Everything is an Object in Python
a = 5 # Integer
b = 5.4 # Float
c = 'apple' #String
d = True # Boolean
e = 0 # Boolean
f = None # None

# Checking types of objects
type(a)
isinstance(a, int)

# Type casting: We can cast one type into another (within reason)
float(a)

# Type casting is not done in place, if you check a again
a
# But if you assign it to another variable, then we have the new variable
j = float(a)
j


int(b)
float(c)
str(a)

'''
Attributes and Methods
Each object has attributes that are unique to the object. E.g. Characters can be capitalised whereas number cannot be.
Numbers can be divided by each other but characters cannot.


Each object also has a set of allowable functions, called methods, which can be used on the object. 
Again, we can raise a number to a power but not a letter so the function of raising to the power is a method unique to a integer or float object.

'''

string = 'hi my name is slim shady'
print(string.upper())

capital_string = string.upper()
capital_string.endswith('SHaDY')

# Do we get a different set of methods if we have a different object
number = 7.5

number.as_integer_ratio()
number.is_integer()

'''
Binary Operators

'''

# We can use operators to find out relationships between objects. These are usually logical operators.
a = 3
b = 4

# AND
((a > 1) & (b < 10))

# OR
((a > 1) | (b < 2))

# EXCLUSIVE OR
((a > 1) ^ (b < 2))

# EQUIVALENCE
a == b

# NOT EQUIVALENCE
a != b

# MATHEMATICAL OPERATORS
print(3**2)
print(5 > 6)
print(5 <= 5)

'''
Strings
'''

string1 = "This is one way to make a string"

string2 = 'This is another way to make a string'

string3 = """
If you have an essay that the world just needs to hear, then you can use
triple double commas and stick what you want in between.
"""

# Notice the escape quotes
string3

# They disappear when printing
print(string3)

intro = "My name is Junaid"

# There are a whole host of String methods we can use
newintro = intro.replace("Junaid", "Jainaba")
newintro

# We can concatenate strings together
'My best friend is ' + 'Junaid'

# We can do this via variable assignment too
first_text = "My best friend is"
name = "Junaid"
first_text + name

# A neat trick is string interpolation, using curly braces {}
string_to_interpolate = 'my name is {}'
string_to_interpolate

string_to_interpolate.format('Junaid')

string_to_interpolate_more = 'my name is {} and I live in the {}'
string_to_interpolate_more.format('Junaid', 'United Kingdom')

string_to_interpolate_more = 'my name is {} and I live in the {}'
name = ''
location = ''
string_to_interpolate_more.format(name, location)

'''
Dates and Times

Datetimes are considered in a special way with Python. 
Dates are not a native base structure but with the datetime library, there is an imported Python structure - called a datetime object.

It's worth going over the full details in the book - from page 44

'''

from datetime import datetime, date, time

# Today's date
today = datetime.today()
today

# We can pull things out of the datetime object
[today.day
,today.minute
,today.microsecond]

# We can format datetime objects to they look like dates that we recognise
today.strftime("%d/%m/%Y %H:%M:%S")

# We can convert properly formatted strings to datetimes
datetime.strptime('19930728', '%Y%m%d')

'''
Control Flow

if, elif and else. The if statement is one of the most well-known control flow statement types. It checks a condition that, if True, evaluates the code in the block that follows.
'''

if x < 0:
    print("Houston we have a negative number")


if x < 0:
    print("Houston we have a negative number")
else:
    print("Houston we have a nonnegative number")


if x < 0: 
    print('negative!')
elif x==0:
    # TODO: put something smart here 
    pass
else: 
    print('positive!')


# An if statement can be optionally followed by one or more elif blocks and a catch- 
# all else block if all of the conditions are False:
if x < 0:
    print('It\'s negative')
elif x == 0:
    print('Equal to zero')
elif 0<x<5:
    print('Positive but smaller than 5')
else:
    print('Positive and larger than or equal to 5')

'''
Loops

There are  2 types of loops; for loops and while loops

'''

# A list is the most basic data structure in Python. 
# We hold things of different types in it
list1 = [1, 2, 3, 11, -9]
list2 = ['apple', 'orange', 'banana']
list3 = [1, 'Junaid', 27, 'Jainaba', ['Junaid', 28, 7, 1993]]

# We can see how large a list is by using the len() function
[len(list1), len(list2), len(list3)]

# We can access elements of a list by using indexing and slicing
# Indexing: Python starts with 0!!
list2[0]

# Slicing: Return all elements in a list from element 1 to before element 4
list3[1:4]
list3[4][0:3] # You can recursively index/ slice

# We can add things to a list using the append method. Things are added at the end.
little_list = [18, 5000000, 0.987]
little_list.append(0.5) # This is added in place

little_list

# We can take things out of a list using the pop method
little_list.pop(2) # Here we specify an index vs a value. Remove something from the 2nd position
little_list

# For loops: These loops are for when we want to perform an operation over a series of elements in an object
# Say we wanted to take the list [1, 2, 3, 11, -9] and multiply every element in it by 2, we also want all numbers to be positive. 
# To do this we need an output empty list in which we will save our result and write the code for our for loop
output_list = [] # Here is an empty list where we want to put our resulting elements in

for element in range(0, len(list1)): # For every element in the range between 0 and the length of our input list
    x = abs(2 * list1[element]) # What should the value be in the output list at this stage?
    output_list.append(x) # Append it to the output list
    
output_list

# While loops: This runs a piece of code iteratively until a condition is met
x = 256
total = 0

while x > 0:
    if total > 500:
        break # Break the if statement
    total += x
    x = x // 2

# 256 + (256 // 2) + (128 // 2) + (64 // 2) + (32 // 2) + (16 // 2)


'''
Importing Modules

In Python, we have base objects and functions which come with the initial install of the language. However there are some functions that we can download which are additional to what we call base Python. 

We do this by installing and importing modules/ libraries/ packages. Then we can extend the reach of Python.

For full information, please see: https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/

'''

# Install a module - Using pip
pip install numpy

# Once a library is installed, it doesn't mean we can use it straight away. We must be imported.
import numpy as np

# Sometimes you will have massive modules where you only want to import some functions
from some_module import f as foo, g as bar

# Once we have a module imported, we can use the functions contained within.
# Since we installed numpy with a prefix np, we can use that as a reference
np.ceil(9.86) # Ceiling function always rounds up to the nearest integer


'''
Built-it Data Structures

In Python we have multiple native data structures
These are VERY important to know so check put Chapter 3 in the book

'''

# We have already seen lists
list1 = ['tinky winky', 'dipsy', 'lala', 'po', [1, 2, 3]]

'''
Tuple
Tuple: A tuple is a fixed-length, immutable sequence of Python objects
They are created with a comma-separated sequence of values
'''

tuple_1 = (9, 11, 4.5)

# We can nest tuples too
nested_tup = ((4,5,6), (7,8))

# We can convert any sequence to iterator into a tuple using the function tuple()
list_converted_tuple = tuple([4, 0, 2])
string_converted_tuple = tuple('string')

# Accessing tuples: We can access tuples with square brackets and are 0-indexed
string_converted_tuple[1]

# Tuples are immutable vs lists
lst = [1, 3, 19]
tup = (1, 3, 19)

# Say we wanted to replace the 3 with a 4
# We can do this with a list
lst[1] = 4

# Say we wanted to replace the 3 with a 4
# We can't do this with a tuple
tup[1] = 4

# We can concatenate tuples just like lists
tup_a = (1, 2, 'foo')
tup_b = (3, 4, 'bar')
tup_a + tup_b

# We can multiple a tuple by a number, like a just a list, and it replicates the elements
tup_j = ('Junaid', 'Butt') 
tup_j * 5

'''
Dictionary

A dictionary or dict in Python is the most important built-in Python data structure. It's also called a hash map or associative array.
It contains a list of pairs called keys and values
'''

# We create dictionaries using curly braces
dict1 = {'Junaid': ['IBM', 400], 'Amin': ['Unknown', None]}
dict1

# We can access, insert or set elements using square brackets but we specify the key by name here
dict1['Junaid']

# Replace an existing element
dict1['Junaid'][1] = 365
dict1

# Insert a new element
dict1['Junaid'].append('Pusher') # Insert my previous workplace
dict1

# Delete an element from a dictionary
del dict1['Junaid'][2]
dict1

# We can access all the keys in a dictionary
dict1.keys() # But this format isn't helpful so we turn them into a list
list(dict1.keys())

# We can access all the values in a dictionary
dict1.values()
list(dict1.values())

# We can merge one dict into another
d1 = {'a': 'some value', 7: 'an integer'}
d2 = {'b': 'foo', 'c': '12'}

d1.update(d2) # Update is done in place so d1 is mutated
d1

# Bonus: Making dictionaries with zip
# Say you have 2 lists  - one of keys and one of values. We can make them into a dictionary using zip
key = ['Junaid', 'Amin', 'Jainaba']
values = [1993, None, 1996]

age_dict = dict(zip(key, values)) # zip pairs them, dict turns them into a dictionary

age_dict

'''
Set

From Mathematics, a set is an unordered collection of unique elements.

For full set of operations, see the chapter.
'''

# A set is created using the set function or curly braces
set([2, 2, 2, 1, 3, 3])
{2, 2, 2, 1, 3, 3}

# Sets support mathematical set operations like union, intersection, difference and symmetric difference
# Make 2 sets
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}

# Union
a.union(b)
a | b

# Intersection
a.intersection(b); a & b


# Check if a set is a subset of the other
a_set = {1,2,3,4,5}
{1,2,3}.issubset(a_set)

'''
Functions

Functions are the primary and most important method of code organisation and reuse in Python.

If you need to repeat the same of very similar code more than once, it is worth writing a resuable function. 

Functions are declared with the def keyword and a result is returned with the return keyword

'''

# Let's define a function to cube a number and add the log of the other
def my_function(x,y):
    z = x**3 + np.log(y) # Variables created inside a function are not created globally
    return z

# Let's use the function
my_function(x = 2, y = 3)

# Inputs to a function are called arguments. In the previous function, x and y are called arguments.
# Arguments can be named anything and we can set some arguments to a default value
def my_sloppy_function(junaid, jainaba, power = 3):
    z = junaid**power + np.log(jainaba)
    return z

# The function gives the same result
my_sloppy_function(junaid = 2, jainaba = 3) # In this function, we assume the default value

# We can change the default argument value too
my_sloppy_function(junaid = 2, jainaba = 3, power = 2)

# We can stick anything inside a function and return it
# Let's make a function to check if an input star sign is Junaid's star sign
def is_junaid_starsign(starsign):
    
    # Change the input to all lowercase
    lc_starsign = starsign.lower()
    
    # Use an if else statement to check if it's my starsign
    if lc_starsign == 'leo':
        z = "This is Junaid\'s starsign yay"
    else:
        z = "This is not Junaid\'s starsign - don't you know astrology is haram!"
        
    return z

# Test the function
is_junaid_starsign('Cancer')

# A function can return multiple values
# Write a function to return capital cities

capitals = ['London', 'Paris', 'Dubai', 'Moscow', 'Madinah', 'Addis Abbaba']

def give_me_cities(x = 'London', y = 'Paris', z = 'Dubai'):
    
    e = 'Moscow'; f = 'Madinah'; g = 'Addis Abbaba'
    
    return x,y,z,e,f,g

give_me_cities(x = 'London', y = 'Paris', z = 'Dubai')

# We can save a function's results to a variable
capital_tup = give_me_cities(x = 'London', y = 'Paris', z = 'Dubai')

# We can save the multiple returned values to multiple output objects
# We can even make functions with no arguments - NOT RECOMMENDED
def useless_function():
    x = list(np.random.poisson(lam = 1, size = 2))
    y = list(np.random.poisson(lam = 1, size = 2))
    
    return x, y

foo, bar = useless_function()

'''
Asking for help

Very often there will be built in functions about which you don't know. We can use the help() function with the function name as the argument to check the Python documentation.

Failing that, it's legitimate to check the internet (stackoverflow)

'''

# Using the help function gives access to Python documentation
help(np.random.poisson)





























































