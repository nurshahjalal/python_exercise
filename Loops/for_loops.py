for i in range (1,20):
    print("i is now {}".format(i))

number = "678,908,097,6543"

for i in range(1, len(number)):
    print(number[i])

# to print only numbers
for i in range(1, len(number)):
    if number[i] in '0123456789':
        print(number[i])

for i in range(1, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')


# Char

name = "Nur Shahjalal"
extractChar = ''
for char in name:
    if char in "abcdefghijklmno":
        extractChar = extractChar + char
print("\n" + extractChar)

# state

for state in ["Nur", "I Don't Know", "Don't Ask Me", "I will Tell You Later"]:
    print ("Where are you Going : " + state)


# nested for loop

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("=================================")


# step

for i in range(1, 100, 20):
    print(i)

# Advance slicing for loop with range
print("**********************************")
for i in range(100[::7]):
    print(i)
for k in range(100)[::7]:
    print(k)