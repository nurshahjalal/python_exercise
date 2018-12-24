
# print squire number of given number
# with regular way with for loop

emptylist = []
for i in range(10):
    emptylist.append(i*i)
print(emptylist)


print("==" * 30)
# same thing can be achieved in one line with the help of list comprehension
squires = [i*i for i in range(10)]
print(squires)

# print squire of even num

even_squires = [i*i for i in range(20) if i % 2 == 0]
print(even_squires)

