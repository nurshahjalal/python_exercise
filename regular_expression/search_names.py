import re
'''
Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers(Minimum, Maximum) 
'''

with open("contact", "r") as f:
    contents = f.read()

    pattern = re.compile(r'Mr\.') # matches only Mr with Dot(.)
    match = pattern.finditer(contents)

    for m in match:
        print(m.group())

    print('=='*45)
    pattern = re.compile(r'Mr\.?')  # matches Mr. and Mr with spaces after
    match = pattern.finditer(contents)

    for m in match:
        print(m.group())

    # matching any name after Mr
    # with + quantifiers it will  not returning Mr. T
    print('==' * 45)
    pat_2 = re.compile(r'Mr\.?\s[A-Z]\w+')  # /s = space
    match_2 = pat_2.finditer(contents)

    for m_2 in match_2:
        print(m_2.group())

    # with * quantifiers it will return 0 or More including Mr. T
    print('==' * 45)
    pat_3 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')  # \w any character following * = 0 or more
    phone_pat = re.compile(r'\d{3}.\d{3}.\d{4}')
    match_3 = pat_3.finditer(contents)
    phone_3 = phone_pat.finditer(contents)

    for m_3 in match_3:
        print("Name     : " + m_3.group())
        for p in phone_3:
            print("Phone    : " + p.group())
            break



