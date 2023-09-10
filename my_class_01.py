"""Object Oriented Programe"""


class Employee:
    """Employee Class"""

    def __init__(self, first, last, pay):  # Attributes of Employee class
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@compny.com"

    def full_name(self):  # Class method
        """Print Full Name"""
        return f"{self.first} {self.last}"


emp_1 = Employee("Jan", "Woo", 5000)  # instance of a class
emp_2 = Employee("Alex", "Core", 6000)  # instance of a class

print(emp_1.full_name())
print(emp_1.pay)
