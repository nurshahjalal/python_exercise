class Employee:

    raise_amount = 1.05

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


class Developer(Employee):

    def __init__(self, first_name, last_name, pay, pro_lang):
        super().__init__(first_name, last_name, pay) # inheriting constructor from employee class using super
        self.pro_lang = pro_lang


dev_1 = Developer("Nur", "Shahjalal", 120000, 'Python')
dev_2 = Developer("Dave", "Smith", 130000, "Java")

print(dev_1.email)
print(dev_1.pro_lang)

print(dev_2.email)
print(dev_2.pro_lang)


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)  # inheriting constructor from employee class using super
        if employees is None:
            employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp_fullname(self):
        for emp in self.employees:
            print("=====> " + emp.fullname())


mgr_1 = Manager("Don", "Walton", 130000, [dev_1])
print(mgr_1.email)
mgr_1.print_emp_fullname()
mgr_1.add_emp(dev_2)

mgr_1.print_emp_fullname()


print(isinstance(mgr_1, Manager))
print(isinstance(dev_2, Employee))
print(issubclass(Developer,Employee))
print(isinstance(mgr_1, Developer))