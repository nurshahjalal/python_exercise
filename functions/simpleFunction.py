def food():
    print("I am eating food")


food()


def return_something():
    return 6


print(return_something())

num = return_something()

print(num)

# With arguments
def print_name(name):
    print(name)


print_name("Nur")



def print_anything(*args, Sep=";"):
    print(args)

print_anything("Nur","Shahjalal")

def center_text(*args):
    text = ""
    for arg in args:
        text += str(arg) + " "
    left_margin = (80 - len(text))
    print(" " * left_margin, text)

center_text("first", "Second", 3, 5, "Nine")



