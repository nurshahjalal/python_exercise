class Employee:
    # init__ is the default constructor
    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@email.com'

    def fullname(self):
        return self.first_name + ' ' + self.last_name


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
