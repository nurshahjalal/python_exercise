class FirstHundredGenerator:

    def __init__(self):
        self.number = 0

    def __next__(self):
        if self.number < 100:
            current = self.number
            self.number += 1
        else:
            raise StopIteration

cl_gen = FirstHundredGenerator()
print(next(cl_gen))
