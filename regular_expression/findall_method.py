import re

with open("contact", "r") as f:
    contents = f.read()
    pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

    # with find all method, no need to use group()
    matches = pattern.findall(contents)
    for match in matches:
        print(match)