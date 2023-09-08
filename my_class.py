""" Object Oriented Progrmming """


class Employee:
    """Employee class tutorial"""

    # Class attribute
    father_name = "Syed Asif"

    def __init__(self, first_name, last_name):
        # instance attribute
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        """Call full name"""
        return f"{self.first_name} {self.last_name}"


# 1st instance of a class
ali = Employee("Ali", "Raza")
# print(ali.first_name, ali.last_name)
print(ali.full_name())
print(ali.father_name)
# # 2nd instance of a class
# maaz = Employee("Maaz", "Haider")
# print(maaz.first_name, maaz.last_name)

# # 3rd instance of a class
# aashir = Employee("Aashir", "Raza")
# print(aashir.first_name, aashir.last_name)
