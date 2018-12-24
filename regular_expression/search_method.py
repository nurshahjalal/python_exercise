import re

with open("contact", "r") as f:
    contents = f.read()
    pattern = re.compile(r'\d{3}.\d{3}.\d{4}')

    # Search method will return only first match
    matches = pattern.search(contents)
    print(matches)