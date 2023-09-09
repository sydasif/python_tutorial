"""Integers and Floats - Working with Numeric Data"""
# Arithmetic Operators
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division:   3 // 2
# Exponent:         3 ** 2
# Modulus:          3 % 2

# Comparisons Operators
# Equale:           3 == 2
# Not Equale:       3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Greater or Equal: 3 >= 2
# Less or Equal:    3 <= 2

int_num = 3  # integer
float_num = 3.14  # float

# Order of operation of arithmetic operators
print(3 * 2 + 1)
print(3 * (2 + 1))

# Increment  a number
num = 1
num += 1
print(num)
num *= 10
print(num)

# built-in function
print(abs(-3))
print(round(3.75))
print(round(3.75, 1))

# Type casting

num1 = "100"
num2 = "200"

num1 = int(num1)
num2 = int(num2)

print(num1 + num2)
