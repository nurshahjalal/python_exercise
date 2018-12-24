
# Tuples usually starts with parenthesis/bracket (), but it can come without bracket as well

tup = "A", "B", "C"
print(tup) # this will print out a tuple = ('A', 'B', 'C')

# Also
print(('A', 'B', 'C')) # this will print out a tuple = ('A', 'B', 'C')

# Once tuple is assigned it cannot be changed, that's why it is immutable

# Tuples consists of heterogeneous data –[ ‘a’, ’b’, ‘c’, 1, 2, 3,]

# Another Example with different data type
welcome = "Hello", "Welcome to my house at",  8636
print(welcome)

# We can use index and slice the tuple
print(welcome[0])
print(welcome[1])
print(welcome[2])

# tuple can be changed ,

name = ("Name", "is", "Nur")
print("Name is {}".format(name))

name = name[0], name[1], "Shahjalal"

print("After changing the Tuple value : Name is {}".format(name))

# Another example of list

metallica = ["Ride the Lighting", "Metalica", 1984]
print(metallica)

title, artist, year = metallica

print(title)
print(artist)
print(year)

# Tuple within a tuple

menuList = "Breakfast", "Lunch", "Dinner", (("Morning", "Egg and Bread", "Coffee"),
                                            ("Noon", "Pasta and Soup", "Coke"),("Evening", "Salad and Fish", "Tea"))


print(menuList)
startOfDay, middleOfDay, endOfDay, items = menuList
print(startOfDay)
print(middleOfDay)
print(endOfDay)
print(items)
print(items[0])
print(items[1])
print(items[2])
morningTime, lunchTime, dinnerTime = items
print(morningTime)
print(lunchTime)
print(dinnerTime)
