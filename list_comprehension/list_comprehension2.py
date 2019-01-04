a = list(range(20))
print(a)

double_num = [x*2 for x in a]
print(double_num)

# build string
name_age = [f'I am {age} years old' for age in double_num]
print(name_age)

names = ['John', 'Ralph', 'Jamie']
lower_name = [ name.lower()for name in names]
print(lower_name)