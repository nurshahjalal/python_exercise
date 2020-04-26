freinds = ['Anna', 'Rose', 'Robin', 'William', 'Ramsey']

# find name which starts with R


def starts_with_r(friend):
    return friend.startswith('R')


# filter (arg 1= function that returns True/False, arg 2 = iterable item)
# Filter returns generator
name_starts_with_R = filter(starts_with_r, freinds )

print(list(name_starts_with_R))

Name_Starts_With_R= filter(lambda name: name.startswith('R'), freinds) # returning a generator
print(Name_Starts_With_R) # printing generator object
print(next(Name_Starts_With_R))
print(next(Name_Starts_With_R))
print(next(Name_Starts_With_R))




