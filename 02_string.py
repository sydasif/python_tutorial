# Print Welcome massage
print("Hello, World!")

# Create a variable with single quote
massage = "Hello, World!"
print(massage)
# Create a variable with backslash
massage = "Bobby's World!"
print(massage)
# Create a variable with double quote
massage = "Bobby's World!"
print(massage)
# Multiline string variable
massage = """Bobby's world was
a good cartoon in 1990s"""
print(massage)
# lenght of a string
massage = "Hello, World!"
print(len(massage))
# Slicing a string
massage = "Hello World"
print(massage[0:5])  # index start from zero
print(massage[:5])  # same as above
print(massage[6:11])
print(massage[6:])  # same as above

# String method ==> Method is function belong to an object.
massage = "Hello, World"
print(massage.lower())  # change to lower case
print(massage.upper())  # change to upper case
print(massage.count("l"))  # count method needs an argument
print(massage.find("World"))  # case sensitive
print(massage.find("Python"))  # if word not find, return -1

# replace word in string
massage = "Hello World"
massage = massage.replace("World", "Python")
print(massage)

# String concatenation
greeting = "Hello"
name = "Bob"

massage = greeting + ", " + name
print(massage)

# String concatenation with formate
greeting = "Hello"
name = "Boby"

massage = "{}, {}".format(greeting, name)
print(massage)

# String concatenation with f-string
greeting = "Hello"
name = "Bob"

massage = f"{greeting}, {name}"
print(massage)

# You can use method in f-string
greeting = "Hello"
name = "BOB"  # upper case
massage = f"{greeting}, {name.lower()}"
print(massage)
