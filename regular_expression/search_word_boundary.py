import re
text_to_search = "Ha HaHa This Is Word Boundary Ha"

''' 
Word boundary means searching for pattern which has whitespace 
using \b
using \B

'''

pat = re.compile(r'\bHa') # looking for a Ha with word boundary - returns 3 Ha from 4 Ha
matches = pat.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print("Searching search result ")
    print(match.group())

# Without word boundary
pat = re.compile(r'\BHa') # looking for a Ha with No word boundary - returns 1 Ha from 4 Ha
matches = pat.finditer(text_to_search)
for match in matches:
    print(match) # return iter object
    print("Searching search result ")
    print(match.group())

