
# The map() function applies a given function to each item of an iterable (list, tuple etc.) and
# returns a list of the results.

def calculateS_suire(n):
    return n*n

numbers = (1, 2, 3, 4)
result = map(calculateS_suire, numbers)
print(list(result))

def length_of_letter(n):
    return len(n)

letters = ("apple", "Banana", "Avocado", "New York")
ln = map(length_of_letter, letters)
print(list(ln))
