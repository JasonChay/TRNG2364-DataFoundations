### DATA TYPES ###
# Variables can be declared implicitly without specifying datatype

# String
a = "string"
explicitString: str = "explicit string"

# Integer
b = 1234
explicitInt: int = 7

# Float
c = 3.14159
explicitFloat: float = 2.71828

# Boolean
# Falsey values: 0, 0.0, None, "", [], (), {}
# Truthy values: anything else
d = True
explicitBool: bool = False
# Use explicits when for example you want a whole number to be treated as a float

# NoneType - None - represents null value
e = None
explicitNone: None = None

# print(bool(e))

# Check datatype of a variable
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))

# Assign multiple variables in one line
dog = DOG = Dog = dOg = "Beagle"
# print(dog, DOG, Dog, dOg)

### NAMING CONVENTIONS ###
# Screaming Snake Case: MY_VARIABLE_NAME
# is used for constants
# Snake Case: my_variable_name
# is used for classes
# Pascal Case: MyVariableName
# is used for everything else

### COLLECTIONS ###
# a module in Python for holding multiple values
# Lists (Array), Tuples, Sets, Dictionaries
# List: ordered, changeable, allows duplicate values
# Tuple: ordered, unchangeable, allows duplicate
# Set: unordered, unchangeable, unindexed, no duplicates
# Dictionary: ordered, changeable, no duplicates

# List
# Python lists are objects with data type 'list'
fruits = ["Orange", "Strawberry", "Apple"]
fruityFruits = favoriteFruits = ["Strawberry", "Apple", "Banana"]
orange, strawberry, apple = fruits
# print(orange, strawberry, apple)

# print(type(fruits))

# Use negative indexing which starts from the end of the list
# print(fruits[-1]) # is the last element in the list

# Range of index
# print(fruits[1:3]) # 1 inclusive 3 is exclusive

# Add at specific index
fruits.insert(2, "Pineapple")
# print(fruits)

# Tuple
# defined as object of datatype 'tuple'
animals = ("Cat", "Dog", "Bird", "Fish")
# print(animals)
# print(type(animals))

# tuples are immutable so no append
# convert tuple to a list first to change it
animals = list(animals)
animals.append("Snake")
# print(animals)

# Set
colors = {"Blue", "Green", "Pink"}
# add() or remove()
colors.add("Yellow")
colors.remove("Blue")
# print(colors) # Sets are unordered 

# Sets support intersection, difference, and union
food = {"Burger", "Fries", "Milkshake"}
morecolors = {"Brown", "Red", "Pink"}
intersectionColors = colors & morecolors
intersectionFood = colors & food

unionColors = colors | morecolors

differenceSet = colors - morecolors

# print(intersectionColors)
# print(unionColors)
# print(differenceSet)

# Dictionary
# key-value pairs
foodDict = {"Sushi": "Fish", "Burger": "Beef", "Pizza": "Pepperoni"}

# print(foodDict.keys())
# print(foodDict.values())

foodDict["Sushi"] = "Rice"
# print(foodDict)

# Add to the dictionary
foodDict["Pickle"] = "Cucumber"

# Check if exists
# if "Burger" in foodDict:
#     print("Yes, there is a burger in the dictionary")

# Operators
# Arithmetic operators: +, -, =, /, %, **, //
# Assignment operators: =, +=, -=, *=, /=, etc.
# Comparison operators: ==, !=, >, <, >=, <=
# Logical operators: and, or, not

# Getting user input()
print("Please enter your name:")
name = input()

# f stands for formatted string
# allows us to paramaterize our string
print(f"Hello {name}")

favColor = input(f"What is your favorite color, {name}?\n")

