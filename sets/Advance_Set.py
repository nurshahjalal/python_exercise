
set_1 = {1, 2, 3, 4, 5}
set_2 = {1, 3, 4, 6, 9, 11}
set_3=(1,2,4)
set_4 = set()
print(type(set_1))
print(type(set_3))
print(type(set_4))
new_set = set_1.difference(set_2)
print(new_set)

# intersection  -- matching between two sets
print(set_1.intersection(set_2))

# Union  -- unique matching and un matching between two sets
print(set_1.union(set_2))

# difference  -- difference from comparing set
print(set_1.difference(set_2)) # difference of set_1 from set_2
print(set_2.difference(set_1)) # difference of set_2 from set_1