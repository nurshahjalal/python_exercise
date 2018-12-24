import re

sentence = 'Start a sentence and ' \
           'Start Sentence ' \
           'then bring it to an end' \
           'then bring it to an end'

'''
^ caret sign - search for beginning in the string
$ search for end of string 

'''
# returns only one match which is found in the beginning
pat = re.compile(r'^Start')
matches = pat.finditer(sentence)

for match in matches:
    print(match.group())


# returns only one match which is found in the end
pat2 = re.compile(r'end$')
matches = pat2.finditer(sentence)

for match in matches:
    print(match.group())