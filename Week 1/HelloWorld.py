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

print(bool(e))

# Check datatype of a variable
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Assign multiple variables in one line
dog = DOG = Dog = dOg = "Beagle"
print(dog, DOG, Dog, dOg)