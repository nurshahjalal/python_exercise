class FirstHundredGenerator:

    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
            return current
        else:
            raise StopIteration

    # To make cl_gen instance iterable
    # this special __iter__ will make any class iterable
    def __iter__(self):
        return self


# All generator is iterator not itarable
cl_gen = FirstHundredGenerator()
#  Next method is calling special method __next__ and remember the last generator
# cl_gen is iterator and not iterable
print(next(cl_gen)) # Generating 0
print(next(cl_gen)) # Generating 1
print(next(cl_gen)) # Generating 2



print(sum(FirstHundredGenerator()))

for i in FirstHundredGenerator():
    print(i)

