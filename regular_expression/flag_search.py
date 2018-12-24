import re

sentence = 'Start a Sentence and start another sentence'
pattern = re.compile(r'Start') # returns only one 'Start' word as Searching with Capital 'S'
matches = pattern.findall(sentence)
print(matches)


pattern = re.compile(r'Start', re.IGNORECASE) # returns all 'Start' word as Searching with ignore case 'S'
matches = pattern.findall(sentence)
print(matches)