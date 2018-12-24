

# in Python range is bult in type

print (range(100))


# Create a number list with range
my_lists = list(range(10))
print(my_lists)

even = list(range(0, 100, 2))
odd = list(range(1, 100, 2))

print("Even Numbers are : {} ".format(even))
print("Odd Numbers are : {} ".format(odd))

sevens = range(7, 10000, 7)

x = input("Please enter a number 1 to 10000: ")
if x in sevens:
    print("{} is divisible by 7".format(x))
else:
    print("{} is NOT divisible by 7".format(x))

small_decimals = range(0, 10)
myRange = small_decimals[::2]
print(myRange)
print(myRange.index(4))

decimals = range(0, 100)
my_range = decimals[3:40:3]

print(my_range == range(3, 40, 3))

# This is also true
print(range(0, 5, 2) == range(0, 6, 2))

print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))

r = range(0, 100)
print(r)
for i in r[::-2]:
    print(i)
