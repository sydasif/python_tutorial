"""Object Oriented Programe"""


class Employee:
    """Employee Class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@compny.com"

    def full_name(self):
        """Print Full Name"""
        return f"{self.first} {self.last}"


emp_1 = Employee("Jan", "Woo", 5000)
emp_2 = Employee("Alex", "Core", 6000)

print(emp_1.full_name())
print(emp_1.pay)
