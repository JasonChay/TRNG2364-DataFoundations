import math
import json
import re

# Math contains useful math constants and functions

# min() and max() work on iterables or amongst multiple arguments
x = min(2, 7, 99, 18, 4)
y = max(6, 17, 81, 100, 42)
print("Minimum value: ", x, "Maximum value: ", y)

# abs() function returns the absolute value of a number
z = abs(-7.23)
print("Absolute value: ", z)

# pow() function returns param1 to the param2 power
a = pow(3, 4)
print("Power: ", a)

# sqrt() 
b = math.sqrt(64)
print("Square root: ", b)

# ceil() rounds up to the nearest int
c = math.ceil(4.2)
print("Ceiling: ", c)

# floor() rounds down to the nearest int
d = math.floor(7.8)
print("Floor: ", d)

# pi constant 
p = math.pi
print("The value of pi: ", p)



# JSON
# JavaScript Object Notation

# parse JSON objects and convert them into Python dicts
json_data = '{"name": "Alice", "age": 30, "city": "New York"}'
data = json.loads(json_data) # .loads() can take string, bytes, or bytesarray
print("Name: ", data["name"])
print("Age: ", data["age"])

# or convert Python dicts into JSON objects
# dict, list, tuple, string, int, float, bool, None 
# can all be converted using dumps()
python_dict = {"Fruit": "Apple", "Color": "red", "Quantity": 5, "test": {"k1": "v1", "k2": "v2"}}
json_object = json.dumps(python_dict)
print("JSON object: ", json_object)

# dumps() function can take additional parameters to format the JSON output
formatted_json = json.dumps(python_dict, indent = 4)
print("Formatted JSON: ", formatted_json)

# If you make a class with fields that are not compatible with JSON, 
# you must make a custom JSON encoder class to use dumps()

# Vice versa, you must create a custom decoder to use loads()
# this one will be a function instead of a class

# RegEx 
# Regular Expression is a sequence of characters that forms a search pattern
# Useful for finding substrings, data validation, text, manipulation
# re module 

# search() search for pattern within a string
text = "The cat and the rat are on the roof with another cat wearing a 3 shoes and 4 collars"
match = re.search("cat", text)
if match: print("pattern found: ", match)

# findall() find all occurrences of the pattern
matches = re.findall("cat", text)
if matches: print("pattern found: ", matches)

# regex metacharacters to perform more complex searches
# aka wildcards
# [] - a set of characters
print(re.findall(r"[cr]at", text)) # [cr] - starting with c or r

# \d - any digit 0-9
print(re.findall(r"\d", text))

# ^ - checks if starts with
print(re.search(r"^The", text)) # checks if the string starts with 'The'

# $ - ends with
print(re.search(r"collars$", text)) # if false returns None

# Look up other metacharacters

# split() function splits string at each match of a pattern
split_text = re.split(r"\s", "Split this text into words")
print(split_text)

# sub() function replaces matches with a specified string
replaced_text = re.sub(r"cat", "dog", text)
print(replaced_text)