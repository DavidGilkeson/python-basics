# Variables are containers for storing data values

# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.

x = 5 # This means x is a type of int
x = "String" # y is type of string

print(x)
# Variables do not need to be declared with any particular type, and can even change type after they have been set.

# Casting
#If you want to specify the data type of a variable, this can be done with casting.

x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

print(type(z))

# String variables can be declared either by using single or double quotes:

x = "David"
# is the same as
y = 'David'

# Variable names are case sensitive

a = 4
# is not the same as
A = 5

""" Variable Names

A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:
A variable name must start with a letter or the underscore character
A variable name cannot start with a number
A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
Variable names are case-sensitive (age, Age and AGE are three different variables) """
# Legal Variables

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# illegal Variables

# 2myvar = "John"
# my-var = "John"
# my var = "John"

#Multi Words Variable Names Variable names with more than one word can be difficult to read.


# Camel Case
# Each word, except the first, starts with a capital letter:

myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:

MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:

my_variable_name = "John"

# Python allows you to assign values to multiple variables in one line:

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output Variables
# The Python print statement is often used to output variables.

# To combine both text and a variable, Python uses the + character:

x = "awesome"
print("Python is " + x)

# For numbers, the + character works as a mathematical operator:

x = 10
y = 15
z = "John"

print(x + y)

# If you try to combine a string and a number, Python will give you an error:

# Global Variables
# Variables that are created outside of a function (as in all of the examples above) are known as global variables.

# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myFunction():
  print("Python is " + x)

myFunction()



# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.

# Also, use the global keyword if you want to change a global variable inside a function.

x = "cool"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)