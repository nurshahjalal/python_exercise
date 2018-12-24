numbers = "123456789"

for char in numbers:
    print(char)

# same thing can be done thru iterator
my_iterator = iter(numbers)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print("===" * 10)
for char in numbers:
    print(char)
for char in iter(numbers):
    print(char)


# using for loop in Iter
day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

iter_day = iter(day)

for i in range(0, len(day)):
    dayName = next(iter_day)
    print(dayName)

