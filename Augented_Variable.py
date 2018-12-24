
# Augmented variable

count = 1
# Regular way
for i in range(1, 100):
    count = count + i
print(count)

# Augmented way
count = 1
for i in range(1, 100):
    count += i
print(count)

count = 1000
for i in range(1, 100):
    count -= i
print(count)

count = 1000
for i in range(1, 10):
    count /= i
print(count)

count = 2
for i in range(1, 10):
    count *= i
print(count)

number = 5
multiplier = 8
answer = 0

# add your loop after this comment
for i in range(multiplier):
    answer += number

print(answer)

