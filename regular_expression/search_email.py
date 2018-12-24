import re

with open ("contact", "r") as f:
    contents = f.read()

    pattern = re.compile(r'[A-Za-z0-9._]+@[A-Za-z0-9-]+\.\w+')

    match = pattern.finditer(contents)
    for m in match:
        print(m.group())