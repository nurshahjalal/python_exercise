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
                 'wordwith@' \


# Search for Any Word Character
# \w
# Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].
print("Searching for any word character  " + ("##" * 60))
pat = re.compile('\w')
matches = pat.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print("Searching search result ")
    print(match.group())
    # it is not returning @

print("# # " * 40)
# \W
# Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].
pat = re.compile('\W')
matches = pat.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print("Searching search result ")
    print(match.group())
    # it is not returning @

