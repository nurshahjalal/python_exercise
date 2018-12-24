import re

text_to_search = '516-516-5167' \
                 '718 718 7189' \
                 '917.917.9178' \
                 '929_929_9290' \
                 '347*347*3478'\
                 '800-011-4444'\
                 '800*999*0001'\
                 'there are some phone number above starts with 3 digit like 111 and they have same ' \
                 'pattern after that but with different special character for separation like ' \
                 'underscore, whitespace, dot like 111_1111 and then 4 digit 1111'


pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') # .(dot) is used to match anything whitespace, underscore,dot etx
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match.group())
print("# * # " * 20 )
print("All Phone Except which has * ")

pat = re.compile(r'\d\d\d[-._]\d\d\d[-._]\d\d\d\d') # using character set [-._] limiting  pattern
matches = pat.finditer(text_to_search)

for match in matches:
    print(match.group())


print("# * # " * 20)
print("Only 800 Numbers")
pat_800 = re.compile(r'[8]00.\d\d\d.\d\d\d\d')

match_800 = pat_800.finditer(text_to_search)
for m in match_800:
    print(m.group())


print("# * # " * 20)
print("Only phone Numbers Starts From 1 to 5")
pat_1_5 = re.compile(r'[0-5]\d\d.\d\d\d.\d\d\d\d')

match_1_5 = pat_1_5.finditer(text_to_search)
for m_1 in match_1_5:
    print(m_1.group())


print("# * # " * 20)
# Now grab only phone number from contact file

with open("contact","r") as f:
    contents = f.read()

    pat = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
    phone_matches = pat.finditer(contents)
    for match in phone_matches:
        print(match.group())

    print("# * # " * 20)
    print("Phone Number starts with a particular number")

    pat_3 = re.compile(r'[3]\d\d.\d\d\d.\d\d\d\d')
    match_3 = pat_3.finditer(contents)
    for m in match_3:
        print(m.group())

    print("# * # " * 20)
    print("Phone Number That Not starts with a particular number")
    # Caret inside a character set [] will return everything except caret has been used before a  digit
    pat_3 = re.compile(r'[^3|8|9]\d\d.\d\d\d.\d\d\d\d') # returns all phone number except starts with 3
    match_3 = pat_3.finditer(contents)
    for m in match_3:
        print(m.group())

    print("# * # " * 20)
    print("Phone Number That Not starts with a multiple number")
    # Caret inside a character set [] will return everything except caret has been used before a  digit
    pat_3 = re.compile(r'[^3|8|9]\d\d.\d\d\d.\d\d\d\d') # returns all phone number except starts with 3,8,9
    match_3 = pat_3.finditer(contents)
    for m in match_3:
        print(m.group())

    print("# * # " * 20)
    print("All Phone Number Using curly bracket")
    # Instead of using each filter, a curly bracket is much easier option. Inside curly bracket a digit returns
    # maximum number of digit -- \d{3} means maximum 3 digit equals to \d\d\d
    pat_3 = re.compile(r'\d{3}.\d{3}.\d{4}')
    match_3 = pat_3.finditer(contents)
    for m in match_3:
        print(m.group())

