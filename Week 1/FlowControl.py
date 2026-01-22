import Functions

# For
list = ["a", "b", "c", "d"]
for element in list:
    print(element)

# While
count = 0
while count < 5:
    count += 1

# If-else
# multiple conditions with elif
# will execute first true block and skip rest
# good for multiple mutually exlusive conditions
score = 75

if score >= 90:
    print("Grade A")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Mission Failed")

# Shorthand if
a = 10
b = 9
print("a is my favorite") if a > b else print("b is my favorite")

# Match-case (known as switch case statements in other langs)
choice = input("select a number between 1 and 3\n")

match choice:
    case "1":
        print("case number 1")
    case "2":
        print("case number 2")
    case "3":
        print("case number 3")
    case _: # the default case if none others are true
        print("input error")

print(Functions.myCat)