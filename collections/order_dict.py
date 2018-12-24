from collections import OrderedDict

d= {}
d = OrderedDict()

d['a'] = 'Apple'
d['k'] = 'King'
d['f'] = 'Fish'
d['g'] = 'Goat'
d['b'] = 'Baby'
d['z'] = 'Zebra'
d['m'] = 'Mommy'
d['e'] = 'Egg'

for k, v in d.items():
    print(OrderedDict(sorted(k, v)))

# regular unsorted dictionary
dd = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

# dictionary sorted by key
print(OrderedDict(sorted(dd.items(), key=lambda t: t[0])))
# OrderedDict([('apple', 4), ('banana', 3), ('orange', 2), ('pear', 1)])
#
# dictionary sorted by value
# OrderedDict(sorted(d.items(), key=lambda t: t[1]))
# OrderedDict([('pear', 1), ('orange', 2), ('banana', 3), ('apple', 4)])
