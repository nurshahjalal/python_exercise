import re

with open("email", 'r') as f:
    text_to_search = f.read()

    pattern = re.compile(r'\d\d\d\.')
    mathes = pattern.finditer(text_to_search)
    for match in mathes:
        print(match.group())