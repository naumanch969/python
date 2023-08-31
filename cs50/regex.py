# import re

# email = input("What's your email? ").strip()

# pattern = r'..*@..*\.edu'
# pattern = r'^.+@.+\.edu$'
# pattern = r'^[^@]+@[^@]+\.edu$'
# pattern = r'^[^@]+@[^@]+\.edu$'
# pattern = r'^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$'
# pattern = r'^\w+@\w+\.edu$'
# pattern = r'^\w+@\w+\.(edu|com|gov|net|org)$'
# pattern = r'^(\w|\.)+@(\w\.)?\w+\.(edu|com|gov|net|org)$'
# if re.search(pattern,email, re.IGNORECASE):
#     print('valid')
# else:
#     print('invalid')

# ^ = startswith
# $ = endswith
# . = any character
# * = 0 or more repitition
# + = 1 or more reptition
# ? = optional
# \ = escape character
# (...) = grouping
# (?:...) = non capturing grouping
# [] = includes 
# [^] = exludes
# \w = any word
# \W = not word
# \d = any digit
# \D = not digit
# \s = whitespace characters
# \S = not whitespace characters

# re.IGNORECASE
# re.MULTILINE
# re.DOTALL

# re.search
# re.match
# re.fullmatch
# re.split
# re.findall




# formatting name
# import re
# name = input("what's you name? ").strip()

# if matches:= re.search(r'^(.+), *(.+)$',name):
#     # last, first = matches.groups()
#     last = matches.group(1)
#     first = matches.group(2)
#     name = f'{first} {last}'
# print(name)




# getting name from the url
# import re
# url = input('URL: ').strip()
# username = re.sub(r'^(https?://)?(www\.)?twitter\.com/','',url)
# print(f'Username: {username}')

import re
url = input('URL: ').strip()
if matches:=re.search(r'^(?:https?://)?(?:www\.)?twitter\.com/([a-zA-Z0-9_]+)$',url, re.IGNORECASE):
    print(f'Username: {matches.group(1)}')