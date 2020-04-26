

def gen_num():
    i = 0
    while i < 100:
        yield i
        i  += 1

g = gen_num()
print(next(g))

def gen_prime():
    i = 0
    while i < 100:
        for n in range(2, i):

            if i%n ==0:
                i += 1


        else:
            yield i
            i +=1


gp = gen_prime()
print(next(gp))
print(next(gp))
print(next(gp))
print(next(gp))
print(next(gp))