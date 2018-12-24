import datetime


class Employee:

    raise_amount = 1.05
    num_of_dev = 0

    # init__ is the default constructor
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@email.com'

    def fullname(self):
        return self.first_name + ' ' + self.last_name

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    # Class Method == always pass the class as default
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Static Method don't pass anything automatically, they just behave as regular method
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


# instance variable are passing
emp_1 = Employee('Nur', 'Shahjalal', '90000')
emp_2 = Employee('Test', 'User', '80000')

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

# calling directly from class
fl_name = Employee.fullname(emp_1)
print(fl_name)

Employee.set_raise_amount(1.04)
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_1.raise_amount)

my_date = datetime.date(2016, 7, 10)
print(my_date)
print(emp_1.is_workday(my_date))


