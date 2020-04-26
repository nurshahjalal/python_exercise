top_friends = ['Abul', 'Babul', 'Kabul']

# find the number in top friend
for f in top_friends:
    print(f)

# another way
print(f'My top friend is {top_friends[0]}')

# using enumerate function -- i is the index to count
for i, f in enumerate(top_friends):
     print(f'My top {i} Friend is {f}')

# enumerate returns generator tuple
gen_enu = enumerate(top_friends)
print(next(gen_enu))

for k, v in gen_enu:
    print(k)
    print(v)