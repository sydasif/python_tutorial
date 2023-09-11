"""Object Oriented Programming --> Creating and Using a Class
Book: Python Crash Course 2nd Edition"""


class Dog:
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over"""
        print(f"{self.name} rolled over.")


dog_1 = Dog("Willie", 6)
# Accessing Attributes
print(f"My dog name is {dog_1.name}.")
print(f"My dog is {dog_1.age} years old.")
# Calling Methods
dog_1.sit()
dog_1.roll_over()
# Creating multiple instances
dog_2 = Dog("Lucy", 3)
print(f"\nMy dog name is {dog_2.name}.")
print(f"My dog is {dog_2.age} years old.")
dog_2.sit()
