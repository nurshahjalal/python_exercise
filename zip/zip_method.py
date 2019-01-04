
list_1 = ["Bread", "Butter", "Cookie", "Pizza"]
list_2 = ["Water", "Soda", "Beer", "Coffee"]

new_list = zip(list_1, list_2)
print(list(new_list))

for a, b in zip(list_1, list_2):
    print(a,b)

