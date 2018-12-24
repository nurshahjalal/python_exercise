import re

text_to_search = 'abcdefghijklmnopqrstuvwxyzabc' \
                 'ABC' \
                 '1234567890' \
                 'Ha HaHa' \
                 'cnn.com' \
                 '516-516-5167' \
                 '718 718 7189' \
                 '917.917.9178' \
                 'Mr. Nur' \
                 'Mr Smith' \
                 'Ms Davis' \
                 'Mrs. Robinson' \


# Search for digit
pat = re.compile('\d')
matches = pat.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print("Searching search result ")
    print(match.group())


# Search for Non digit
print("Searching for non Digit " + ("##" * 60))
pat = re.compile('\D')
matches = pat.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print("Searching search result ")
    print(match.group())
