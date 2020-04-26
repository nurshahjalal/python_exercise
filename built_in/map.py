friends = ['Alam', 'kabir', 'alan', 'Alex', 'Conor', 'jisan','Nobi', 'den', 'poland','Liyana', 'Pepa', 'ronaldo']

# regular function to find out the name starts with lower case letter
lower_name = []
for name in friends:
    if name[0].islower():
        lower_name.append(name)

print(lower_name)

# list comprehension
friends_with_lower_case = [name for name in friends if name[0].islower()] # returns a list
print(friends_with_lower_case)

# generator comprehension -- returns an iterator
friends_with_lower_case_letter = (name for name in friends if name[0].islower())
print(next(friends_with_lower_case_letter))

# using map
fl = map(lambda n: n[0].islower(), friends)
print(next(fl))
print(next(fl))
