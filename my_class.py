"""Object Oriented Programe"""


class Employee:
    """Employee Class"""

    num_of_emp = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@compny.com"

        Employee.num_of_emp += 1

    def full_name(self):
        """Print Full Name"""
        return f"{self.first} {self.last}"

    def applay_raise(self):
        """Raise Employee Pay"""
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Jan", "Woo", 5000)
emp_2 = Employee("Alex", "Core", 6000)

print(Employee.num_of_emp)
