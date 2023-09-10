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


class Developer(Employee):
    """Child Class of Employee"""

    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # super method take all attributes from parent class
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):
    """Child Class of Employee"""

    def __init__(self, first, last, pay, employees=None):
        # super method take all attributes from parent class
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        """Add Employee"""
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        """Remove Employee"""
        if emp in self.employees:
            self.employees.remove(emp)

    def prin_emp(self):
        """Print Employee"""
        for emp in self.employees:
            print("-->", emp.full_name())


dev_1 = Developer("Jan", "Woo", 5000, "Python")
dev_2 = Developer("Alex", "Core", 6000, "Java")

mngr = Manager("Sue", "Dee", 9000, [dev_1])

# print(help(Developer))  # help on class

mngr.add_emp(dev_2)
mngr.prin_emp()
