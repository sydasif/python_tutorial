"""Convert Temperature"""


def convert_cel_to_far(degree):
    """Convert celsius to fahrenheit"""
    converted_output = (float(degree) - 32) * 5 / 9

    return converted_output


user_data = input("Enter a temperature in celsius: ")
data = convert_cel_to_far(user_data)
print(f"{user_data} degrees C = {data:.2f} degrees F")


def convert_far_to_cel(degree):
    """Convert fahrenheit to celsius"""
    converted_output = float(degree) * 9 / 5 + 32
    return converted_output


user_data = input("Enter a temperature in fahrenheit: ")
data = convert_far_to_cel(user_data)
print(f"{user_data} degrees F = {data:.2f} C")  # round function can be used
