# Errors and Exceptions
# All exceptions are errors, but not all errors are exceptions

# Errors - problems that prevent our application from running correctly
# Ex. syntax error: there is no handling this problem, you just have to fix it
# comes with error messages to help diagnose the issue
# syntax, indentation, name, value, type 0 division error, etc.

# Exceptions - problems that are raised during runtime and can be handled using try-except (try-catch in Java)

try:
    x = int("Ribs")
except ValueError:
    print("Conversion has failed")

print("After the try-except block") # still prints either way

try:
    number = int(input("Please enter a number\n"))
    result = 10/number
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by 0")

# It is a good idea to have a generic catch-all exception block to handle anything we haven't thought of
except Exception:
    print("I have no idea how you got here")
else:
    # Runs if no exception occurs
    print(f"Result: {result}")

finally:
    # Runs no matter what
    print("Execution complete")

# We can manually throw exceptions using raise
# y = -5
# if y < 0:
#     raise Exception("Sorry, no negative numbers allowed")

# We can create custom exceptions by creating our own exception class

class myCustomException(Exception):
    def __init__(self, message = "This is not the exception you are looking for"):
        super().__init__(message)

userNumber = input("Please enter your favorite integer\n")
if type(userNumber) is not int:
    raise myCustomException()

print(userNumber)