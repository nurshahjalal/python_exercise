from collections import defaultdict


# this is an empty dictionary , no key and value
d = defaultdict(object)
print(d)

# Since Key1 was never assigned as key in dictionary d, hence it will not throw error
print(d['key1'])

# assigning a default value, always return 0 unless assigned
d = defaultdict(lambda: 0)

# will return 0 as default value is 0
print(d['key1'])
