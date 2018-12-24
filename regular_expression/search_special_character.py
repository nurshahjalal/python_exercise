import re

# . -- Return Any character except new line

with open("email", "r") as f:
    text_to_search = f.read()

# to search special character use backslash \, dot(.) will return everything unless a escape character is not used
# a backslash/escape will make sure to return a literally where a dot has been used
pattern = re.compile('.') # returns everything
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print(match.group())

print('**' * 60)
pattern2 = re.compile('\.') # returns where only where dot has been used
matches = pattern2.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print(match.group())

print('**' * 60)
pattern3 = re.compile('@') # returns where only where dot has been used
matches = pattern3.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print(match.group())