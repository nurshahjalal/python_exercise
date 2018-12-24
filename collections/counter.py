
from collections import Counter

num = [1,2,3,4,5,6,7,8,9,0,7,8,9,5,6,67,7,7,7,7,7,7,7,7,7,4,4,4,45,5,5]
print(Counter(num))

word = 'adnvjdfkdfkflriuhkfjfksdaflsdfkdjnflsdkfnsdkfuhiureytrdkndsndinfksdmb'
print(Counter(word))
print(type(Counter(word)))

content = "I am learning python for fun so that i can automate lots of stuff, python is very easy to learn, python a " \
          "great language"
c = Counter(content.split())
print(c)

# print most common word
print(c.most_common(1))

# To find how many times 'nur' has been used , if not 0
print(c['nur'])

# to print unique element
print(list(c))

# to print sum of all counter
print(sum(c.values()))




