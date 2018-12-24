
# Regular method with *args
def car(*args):
    print(args)


# passing as many arguments with the help of *args syntax
car("blue", "Four Cylinder", "AWD")
# result : ('blue', 'Four Cylinder', 'AWD')


def newcar(*args, **kwargs):
    print(args,kwargs)


newcar("Black", "Two Door", "6 cylinder" , horsepower=360, model="Tesla")
# result : ('Black', 'Two Door', '6 cylinder') {'horsepower': 360, 'model': 'Tesla'}
