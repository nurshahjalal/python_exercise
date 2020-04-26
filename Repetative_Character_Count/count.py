
import collections

freq = collections.Counter("Aabcsdddeerrtttdaaa")
for k in freq:
        print(freq[k], k)

print(freq)


# Another way to count duplicate name
names = ['abul', 'babul', 'kabul', 'chulbul', 'abul', 'Babul', 'Nupur', 'nupur', 'kabul', 'abul', 'babul', 'kabul', \
        'chulbul', 'abul', 'Babul', 'Nupur', 'nupur', 'kabul', 'Kabita']

set_names = set(names)

for n in set_names:
    nn = names.count(n)
    print(f'{n} found {nn} times')