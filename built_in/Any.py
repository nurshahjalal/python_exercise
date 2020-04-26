letters = ['a', 'b', 'c', 'd', 'e', 'f', 'r', 'k', 'u', 'z']

num = [1, 2, -3, 0, 9]
# if x > 0 from any value in num, return true
gen_any = any(x>0 for x in num)
print(gen_any)
gen = (x>0 for x in num) # return a list
print(gen) # return true if any of iterable is true meaning

for g in gen:
    print(g)