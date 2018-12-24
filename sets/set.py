# Sets in Python. The data type "set", which is a collection type, has been part of Python since version 2.4.
# A set contains an unordered collection of unique and immutable objects. The set data type is, as
# the name implies, a Python implementation of the sets as they are known from mathematics.


riverFish = {"Large Mouth Bass", "Telapia", "Rui", "Shing"}
print(riverFish)
OceanFish =set(["Striped Bass", "Porgy", "Blue Fish", "Mackerel", "Black Fish"])
print(OceanFish)

# To Add new element in set
OceanFish.add("Shark")
print(OceanFish)

# To create an empty Set
empty_Set = set()
