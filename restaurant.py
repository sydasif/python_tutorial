"""Try It Yourself --> Python Crash Course

9-1. Restaurant: Make a class called Restaurant. The __init__() method for 
Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of 
information, and a method called open_restaurant() that prints a message 
indicating that the restaurant is open. Make an instance called restaurant 
from your class. Print the two attributes individually, and then call both methods.

9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three 
different instances from the class, and call describe_restaurant() for each 
instance.

9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored 
in a user profile. Make a method called describe_user() that prints a summary 
of the user's information. Make another method called greet_user() that prints 
a personalized greeting to the user.
Create several instances representing different users, and call both methods 
for each user"""


class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")


restaurant_1 = Restaurant("Monal", "Fast Food")
print(restaurant_1.restaurant_name, restaurant_1.cuisine_type)
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
print()
restaurant_2 = Restaurant("Shelton", "Street food")
print(restaurant_2.restaurant_name, restaurant_2.cuisine_type)
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()
print()  # print empty line


class User:
    def __init__(self, first_name, last_name, school_name):
        self.first_name = first_name
        self.last_name = last_name
        self.school_name = school_name

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is studying in {self.school_name}.")

    def greet_user(self):
        print(f"{self.first_name} {self.last_name}, glad to see you.")


ali = User("Ali", "Raza", "FIC Kohat")
aashir = User("Aashir", "Raza", "FIC Kohat")
maaz = User("Maaz", "Haider", "NRS Kohat")

ali.describe_user()
ali.greet_user()
print()
aashir.describe_user()
aashir.greet_user()
print()
maaz.describe_user()
maaz.greet_user()
