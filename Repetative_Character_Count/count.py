
import collections

freq = collections.Counter("Aabcsdddeerrtttdaaa")
for k in freq:
        print(freq[k], k)

print(freq)