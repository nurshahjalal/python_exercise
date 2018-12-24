#Simply reduce function takes a list and return an item based the action of the function.

from functools import reduce
num = [3, 7, 8, 90, 76]

new_num = reduce(lambda x, y: x+y, num)
print(new_num)