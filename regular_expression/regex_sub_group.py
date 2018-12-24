import re

urls = '''
https://www.sandata.com
http://www.mydomain.com
http://Testyour1Domain.net
https://nasa.gov
'''

pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern.sub(r'\2\3', urls)
print(subbed_urls)
