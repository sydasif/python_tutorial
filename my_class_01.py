"""Object Oriented Program
1st tutorial --> Creation"""


class Employee:
    """Employee Class"""

    # Instance attributes
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

    # Instance method
    def full_name(self):
        """Print Full Name"""
        return f"{self.first} {self.last}"


# instance of a class
emp_1 = Employee("Jan", "Woo", 5000)
emp_2 = Employee("Alex", "Core", 6000)

print(emp_1.full_name())
print(emp_1.pay)
