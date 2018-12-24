name = input("Please enter your name")
age = int(input("How Old are you {0}".format(name)))
print(age)

if age >= 18:
    print("You are old enough to Vote")
else:
    print("Please come back in {0} Years".format(18 - age))

# and

age = int(input("How Old Are You"))

if (age >= 18) and (age <= 65):
    print("you are good to go")

# Same Command , much shorter way

if 18 <= age <=65:
    print("you are good to go")
    
# NOT Keyword
# NO Boolean TestData Type in Python

if not age == 16:
    print("No Sweet Sixteen")

