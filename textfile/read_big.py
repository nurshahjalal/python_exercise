# reading a big file : instead of reading whole file at a time, reading the 100 character at a time.

with open("big.txt", "r") as rf:
    # reading 100 character at a time
    size_to_read = 10000
    contents = rf.read(size_to_read)
    i = 1
    while len(contents) > 0:
        new_contents = str(i) + ") " + contents
        print(new_contents, end='')
        i = i+i
        contents = rf.read(size_to_read)






