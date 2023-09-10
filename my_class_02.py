"""Object Oriented Programe
2nd tutorial --> Class attributes"""


class Employee:
    """Employee Class"""

    # Class attributes
    num_of_emp = 0
    raise_amount = 1.04

    # Instance attributes
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f"{first}.{last}@company.com"

        Employee.num_of_emp += 1

    # Instance method
    def full_name(self):
        """Print Full Name"""
        return f"{self.first} {self.last}"

    def applay_raise(self):
        """Raise Employee Pay"""
        self.pay = int(self.pay * self.raise_amount)


# instance of a class (object)
emp_1 = Employee("Jan", "Woo", 5000)
emp_2 = Employee("Alex", "Core", 6000)

emp_1.raise_amount = 1.05

emp_1.applay_raise()
print(emp_1.pay)
