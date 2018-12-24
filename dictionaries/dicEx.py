# Dictionary is unordered collections of data and guaranteed for no duplicate data. Dictionary contain key value pair.
# Dictionary value cannot be accessed by index, it is accessed by key.

# Dictionary starts with curly bracket

fruit = {"orange": "a citrus fruit",
            "apple": "good for making cider",
            "lemon": "Sour, a yellow citrus fruit",
            "grape": "a sweet fruit",
            "lime": "a sour, green citrus fruit"}

print(fruit)

print(fruit["grape"])

car={"color": "Red", "Cylinder": 4}
print(car["Cylinder"])

fruit["pear"] = "an odd shape apple"

fruit["lime"] = "a great stuff"
print(fruit)

del fruit["lemon"]
print(fruit)


# To delete all entry but keep an empty dictionary
fruit.clear()
print(fruit)

# To delete entire dictionary
# del fruit

vegetableColor = {"Carrot": "Red", "Spinach": "Green", "Eggplant": "Black", "Potato": "White"}


# Looping the key and items in dictionary
for key, value in vegetableColor.items():
    print(key, value)
print("==" * 20)

for k in vegetableColor:
    print(k)

for vegCol in vegetableColor:
    print(vegetableColor[vegCol])

# To make ordered keys

ordered_keys = list(vegetableColor.keys())
print(sorted(ordered_keys))
for keys in sorted(ordered_keys):
    print(keys)


f_tuple = tuple(vegetableColor.items())
for snack in f_tuple:
    item, color = snack
    print(item + " is " + color)

