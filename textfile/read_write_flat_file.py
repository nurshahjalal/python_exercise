
# open with context manager "with", the advantages of context manager is user can read and write in
# one line and file will be closed automatically.
with open("TestScript.txt", "r") as f:
    content = f.readline()
    all_content = f.readlines()

    print(content)
    print(all_content)

    for line in all_content:
        print(line, end="")

print("==" * 30)
# another way to open a file
file = open("TestScript.txt", "r")
print(file.readline())


print("#" * 30)


with open("TestScript.txt", "r") as rf:
    size_to_read = 10
    all_lines = rf.read(size_to_read)

    while len(all_lines) > 0:
        print(all_lines, end='')
        all_lines = rf.read(size_to_read)
print("#" * 30)


# Seek Method :
# seek method always go back to initial position where it started

with open("TestScript.txt", "r") as new_file:
    size_to_read = 10
    print(new_file.read(size_to_read))
    new_file.seek(0)
    print(new_file.read(size_to_read))






