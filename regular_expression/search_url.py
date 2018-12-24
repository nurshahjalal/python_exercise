import re

urls = '''
https://www.sandata.com
http://www.mydomain.com
http://Testyour1Domain.net
https://nasa.gov
'''


# https? = make 's' optional , will return both 'http' and 'https'
# (www\.)? = make entire group optional, return domain name with/without 'www'
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
match = pattern.finditer(urls)

for m in match:
    print(m.group())


# print only domain name excluding http and www
# using group
# group(0) returns entire result
pat = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
match = pat.finditer(urls)

for m in match:
    print("Group(0) = " + m.group(0))
    print(m.group(2) + m.group(3))