from abc import ABC, abstractmethod

# Python is an OOP

class Animal:
    # In Python we have to override the __init__() to create our constructor
    # Double leading and trailing underscores are used for special methods  
    # Python calls automatically in certain situations ex. __str__(), __len__()
    
    # Passing in self references the freshly created object in our constructor
    def __init__(self, name, age):
        self.name = name # This field is public
        self.__age = age # Double underscores means private property

    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("age must be greater than 0")

    def speak(self):
        return "the Animal made a noise"
        
    def introduction(self):
        return f"My name is {self.name}. I am {self.get_age()} years old."

Bob = Animal("Bob", 3)
print(Bob.introduction())

# ---------------
# Pillars of OOP: Abstraction, Inheritance, Polymorphism, Encapsulation
# Abstraction - the idea of showing only what the user needs to know and hiding the implementation details
# Inheritance - child classes can reuse and extend the behavior of our parent classes
# Polymorphism - (many forms) meaning one interface but multiple implementations
# Encapsulation - the practice of bundling data/attributes and methods into a single unit called a class and restricting access
    # Access Control:
        # Private members: __attribute or __method
         # intended for internal use within the class
        # Protected members: _attribute or _method
         # intended for use within the class and its subclasses
         # not strictly enforced by the language
    
# ---------------

# Inheritance demonstrtation inheriting Animal
class Dog(Animal):
    def __init__(self, name, age, breed, color="Brown"): # color has a default value
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.breed = breed
        self.color = color
    
    # Polymorphism example - overriding
    def speak(self):
        return f"{self.name} barked at the mailman."

    # __str__ acts as toString() method
    def __str__(self):
        return f"My name is {self.name}. I am a {self.color} {self.breed}."
    
Major = Dog("Major", 7, "German Shepherd", "Black")
print(Major)

# Classes can inherit from multiple classes using comma separated list
class Cat(Dog):
    """
    This is an example of a docstring.
    It is common practice to give a brief description of the class in the docstring.

    This class Cat inherits Dog and implements cat-like behavior
    """


    def __init__(self, name, age, breed, color, hairLength):
        # Call parent class using super
        super().__init__(name, age, breed, color)
        self.hairLength = hairLength
    
    def scratch(self):
        return f"{self.name} has scratched the door frame."
    
    def speak(self):
        return f"{self.name} meowed at the door."

Ash = Cat("Ash", 2, "Maine Coone", "Gray", "Medium Hair")
print(Ash.set_age(3))
print(Ash.get_age())

# del keyword to delete either instance attributes or objects 
del Ash.name
# print(Ash) # throws error

# Class methods
# operate on the class itself instead of individual instances.
# can access and modify class attributes but not instance attributes
# decorated with @classmethod and passed cls as first argument

class Student:
    school_name = "ABC School" # class attribute

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

print(Student.school_name)
Student.change_school_name("Different School")
print(Student.school_name)

# Abstraction
# import abc 
# ABC is abstract base class
# abstract methods are notated with @abstractmethod decorator

class Vehicle(ABC):
    """
    Docstring for Vehicle
    inheriting ABC means that this class is abstract and cannot be instantiated
    """
    @abstractmethod
    def start():
        pass

    @abstractmethod
    def stop():
        pass

class Car(Vehicle):
    """
    Docstring for Car
    """
    def start(self):
        print("Starting car engine.")
    def stop(self):
        print("Stopping car engine.")

class Motorcycle(Vehicle):
    """
    Trying to instantiate this class will fail since it does not implement all abstract methods
    """
    def start(self):
        print("Kick-starting motorcycle.")

car = Car()
car.start()
car.stop()

