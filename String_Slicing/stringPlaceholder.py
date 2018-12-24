
age = 30
print("my age is {0} Years".format(age))

print("There are {0} days in the following months {1},{2},{3},{4}".format(31,"January","March","May","June"))

print("""january:{2}
February:{0}
March:{2}
April:{1}
May:{2}
June:{1}
July:{2}
August:{2}
September:{1}
October:{2}
November:{1}
December:{2}""".format(28,30,31))

print("My age is %d years" %age)

# %d == Integer
# %s = String

print("My age is %d %s, %d %s" % (age, "Years", 6, "Months"))

for i in range(1, 12):
    print("No {} squired is {} and Cubed is {:4}".format(i, i**2, i**4))

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])

flower = 'blue violet'
print('blue' in flower)