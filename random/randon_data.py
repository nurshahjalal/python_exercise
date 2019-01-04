import random
from random import randint

value = random.random()
print(value)

# random floating value within a range

value1 = random.uniform(1, 10)
print(value1)

# random integer 4r54 value within a range

value1 = random.uniform(1, 10)
print(value1)

print(random.randint(1, 6))

from random import randint

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
n = 8
range_start = 10**(n-1)
range_end = (10**n)-1
print(str(randint(range_start, range_end)))