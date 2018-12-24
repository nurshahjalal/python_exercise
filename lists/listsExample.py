

colorsList = ["red", "black", "white", "orange", "pink", "yellow" ]

for color in colorsList:
    print(color)


evenNum = [2, 4, 190, 56, 98, 10]
oddNum = [1, 7, 19, 11, 13, 97, 103, 75]

# Adding two list
withoutSortNewList = evenNum + oddNum
newList = evenNum + oddNum

print(newList)

# Sorting new list
newList.sort()
print("After sorting all Number in list {} : ".format(newList))

# Same result with Sorted method
print("After sorting all Number in list {} : ".format(newList))

# Compare Lists

if withoutSortNewList == newList:
    print("lists are equal")
else:
    print("Lists are not equal")

# Empty list: =======================================================================
list_1 = []
list_2 = list()

print("list 1 : {}".format(list_1))
print("list 2 : {}".format(list_2))

if list_1 == list_2 :
    print("lists are equal")

# Create a list from a sentence ===========================================================

print(list("This is a list"))

even = [2, 4, 6, 8]
anotherEven = even
print(anotherEven is even)

anotherEven.sort(reverse=True)
print("anotherEven is : {} ".format(anotherEven))
print("even is : {} ".format(even))

# Create Two lists under one list

odd = [1, 3, 5, 7]
evenN = [2, 4, 6, 8]
numbers = [odd, evenN]
print(numbers)

for number_set in numbers:
    print("numbers are {} ".format(number_set))
    for item in number_set:
        print("items are in numbers_set are {} :".format(item))




