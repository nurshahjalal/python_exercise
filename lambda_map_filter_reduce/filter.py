

num = [1, 2, 3, 4, 5, 6, 7, 8, 90, 67, 43, 44, 76, 32, 78, 21, 89, 0]

even_num = filter(lambda x: x%2==0, num)
print(list(even_num))

words = ["Apple", "cat", "Bowling", "New", "adam"]
upper_word = filter(lambda x: x[0]== "A", words)
print(list(upper_word))

