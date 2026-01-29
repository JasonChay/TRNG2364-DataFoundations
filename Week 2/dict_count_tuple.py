# In Python, we can have NAMED tuples
# allows you to access their elements by name and index
# Named tuples are part of the collections module and provide
# a way to create self-documenting, immutable data structures
# Good for reading an object or rows from SQL queries, CSVs, or API responses

from collections import namedtuple, OrderedDict, Counter

# to create a named tuple, we use the namedtuple() factory function
Point = namedtuple('Point', ['x', 'y'])

# We can create an instance of point
p = Point(x=1, y=5)

# Access using a field name
print(p.x, p.y)

# Access items using index
print(p[0])

# Access using getattr()
print(getattr(p, 'y'))

# More applicable example
User = namedtuple("User", ['id', 'username', 'password', 'email'])
myUser = User(12, 'JonDoe', 'password', 'jondoe@email.com')

print(myUser.username, myUser.password)

# Ordered dictionaries
# are good for when you are using items in a specific order
# most common used for configuration settings or environment variables
# also from collections module

config = OrderedDict()

# Set defaults
config["timeout"] = 5
config["retries"] = 3
config["two-factor"] = True

# we can override values that are already set
config["timeout"] = 10

# Set certian items to always be last
config.move_to_end("timeout")

# we can inspect the order
for key, value in config.items():
    print(key, value)

# Counters
# allow us to count things without writing loops
# on iterables
# comes from collections module

words = ["Fruit", "Meat", "Veggies", "Dairy", "Grains", "Legumes"]

words.append("Fruit")
words.append("Fruit")

count = Counter(words)
print(count)
print(count["Fruit"]) # count for a specific element