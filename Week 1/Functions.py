import array as ar

# Functions
def addition_function(x:int, y:int): # expect parameters of type int BUT does not enforce
    return x + y

def bark():
    print("woof")

# print(addition_function(9, 10))
# bark()

# print(addition_function("9", "abc")) # note that this still works and concats the strings

# Scope
# Local: variable declared inside a block are only available inside that block
def local_variable():
    msg = "Yo" # local var
    print(msg)

    def enclosed():
        msg = "enclosed Yo"
        print(msg)

    enclosed()
    print(msg)

local_variable()

# Global: accessed from anywhere within the file
# and even other files if they are brought in via import

myCat = "Wonton"

# Default: anywhere
# Built in default Python methods where all keywords live
# ex. len() type()

# Modules are files in which Python code is written
# to use different modules, we have to import them into the module we want to use it form
# supports aliasese using 'as'

# Arrays are not technically built into python, we have to import array module
# array(typecode, initializer)

# Typecode: this is a single character that specifies the type of data stored in the array
# 'i' : stored integer (4 bytes)
# 'f' : floating point (4 bytes)
# 'd' : double precision floating point (8 bytes)
# 'b' : signed integer (1 byte)
# 'u' : unicode character (2 bytes)
# 'l' : signed long integer (4 bytes)

# Initializer: this is an optional parameter that initializes the array with elements
# it can be a list, tuple, or any other iterable containing the initial values for the array

intArray = ar.array('i', [1, 2, 77, 3, 25, 99, 51])
print(intArray[2])
mySubset = intArray[0:4]
print(mySubset)

for item in intArray:
    print(item)

# sort array in ascending
print(sorted(intArray))

# Lambda function AKA anonymous functions
# small, single line functions that can have any number of arguments, but only a single expression
# lambda args: expression

add = lambda x, y: x + y
print(add(3,4))

pokedex = [
    ("Bulbasaur", 1),
    ("Lapras", 131),
    ("Eevee", 133),
    ("Cubone", 104),
    ("Gengar", 94)
]
pokedex.sort(key=lambda x: x[1], reverse = False)
print(pokedex)