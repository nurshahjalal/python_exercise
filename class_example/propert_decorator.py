class company:

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullname(self):
        return self.fname + " " + self.lname

    # this is very traditional and to get email address every class need to call this method.
    def print_email(self):
        return self.fname + "." + self.lname + "@company.com"

    @property
    def email_address(self):
        pass



emp_1 = company("Ameer", "Gulam")

print(emp_1.fullname())
print(emp_1.print_email())

