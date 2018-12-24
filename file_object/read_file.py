
import random
with open("TestScript.txt", "r") as f:

    contents = f.read()
    print(contents)
    line = f.readline()
    print(line)
    lines = f.readlines()
    print(lines)

    # to read just first 100 character of this file
    print(f.read(100))

with open("TestScript.txt", "a") as a:
    new_line = a.write(str(random.random))
