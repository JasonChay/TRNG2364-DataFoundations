import json

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self) -> str:
        return f'MyClass(name={self.name}, age={self.age})'

# This class will be used in the dumps function
class MyEncoder(json.JSONEncoder):
    # Make sure to implement a function called default
    def default(self, obj):
        if isinstance(obj, MyClass):
            # If the MyClass fields were not compatible with JSON, then we would need to craft a
            # custom dictionary to return here
            return obj.__dict__
        # Return the result of the JSONEncoder default function if this encoder is used with
        # an incompatible class
        return super().default(obj)

my_obj = MyClass("Bob", 30)

my_json = json.dumps(my_obj, cls=MyEncoder)

print(my_json)

# This function will be used to convert JSON data into a MyClass object
def from_json(json_data):
    # This checks if the json_data dictionary has both 'name' and 'age' keys
    if 'name' in json_data and 'age' in json_data:
        # This creates an object of MyClass and returns it with fields initialized
        return MyClass(json_data['name'], json_data['age'])
    # This returns the json_data dictionary if it doesn't have both 'name' and 'age' keys
    return json_data

json_data = '{"name": "Sally", "age": 30}'

# The object_hook parameter is used to tell the json.loads function to use the from_json function
# to convert the JSON data into a MyClass object, if it can
my_object = json.loads(json_data, object_hook=from_json)
print(my_object)