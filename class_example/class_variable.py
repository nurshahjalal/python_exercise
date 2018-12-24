import class_example.class_with_constructor


class Developer:

    raise_amount = 1.05
    num_of_dev = 0

    def __init__(self, first_name, last_name, pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@email.com'
        # To count number of developer added
        Developer.num_of_dev += 1

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


dev_1 = Developer("Python", "Dev", 120000)
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
print("==" * 20)
dev_2 = Developer("TestData Analyst", "Senior Dev", 150000)
print(dev_2.pay)
dev_2.apply_raise()
print(dev_2.pay)
print("==" * 20)
print(dev_1.__dict__)
print("==" * 20)
Developer.raise_amount = 1.05
print(Developer.raise_amount)
print(dev_1.raise_amount)
print(dev_2.raise_amount)
print("==" * 20)
dev_1.raise_amount = 1.06
print(Developer.raise_amount)
print(dev_1.raise_amount)
print(dev_2.raise_amount)

print("==" * 20)

print(Developer.num_of_dev)


# print(int(100000*10.04))
#print(class_example.class_with_constructor.Employee.fullname(dev_1))
