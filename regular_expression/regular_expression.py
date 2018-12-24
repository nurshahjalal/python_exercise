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


sentence = 'Start a sentence and then bring it to an end'
email = 'These are the email addrss we will be testing in regular expression example' \
        'nurShahjalal@pytho.com ' \
        'nur.shahjalal@python.net' \
        'nur_shahjalal@python.org' \
        'Nur_Shahjalal@pyhton.edu' \
        'end of emmail address'

# using find iter method , search for only abc pattern
# it case sensetive, maintaining  sequence, it will not returning cba or bac

pattern = re.compile('abc')
matches = pattern.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print(match.group())

print('**' * 60)





