with open("new_file.txt", 'w') as wf:
    new_text = wf.write("Hello I am New\n" * 10)

# Append Mode, it will append the file
with open("new_file.txt", 'a') as awf:
    awf.write("Hello I am New2\n" * 10)



