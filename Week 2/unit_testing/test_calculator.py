# Name our test files using test_... OR ..._test.py
# the module searches for files with the 'test' in the file name beginning or ending

# Need 2 imports for testing with pytest
# pytest itself, and the code from the module we are testing

# Unit testing llows us to test the smallest portion of our code ("bite-sized pieces")
# Unit test directly call the code uner the test
# this introduces some considerations for when your code communicates with other systems
# external APIs, databases

import pytest
# import only the functions needed for testing
from calculator import add, subtract, multiply, divide

# naming conventions for python tests
# test_{method name}_{what we are testing for}

def test_add_success():
    # unit tests typically follow a A-A-A structure
    # Arrange, Act, Assert

    # Arrange - any variables or test data that we need to set up
    x = 4
    y = 8

    # Act - call the code under test
    result = add(x, y)

    # Assert - we know what we should get back
    # we assert that the result is what was intended
    assert result == 12

def test_divide_success():
    # Arrange
    x = 4
    y = 2

    # Act
    result = divide(x, y)

    # Assert
    assert result == 2

def test_divide_divide_by_zero_exception():
    # Arrange
    x = 400
    y = 0

    # Act
    with pytest.raises(ValueError) as ex:
        # call the method within this with
        divide(x, y)

    # Assert
    # Cast to a string for easy comparison
    assert str(ex.value) == "Cannot divide by 0"