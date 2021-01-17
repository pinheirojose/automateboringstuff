import re

message = 'Call me 415-555-1001, or at 415-555-9999'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message) #match object
print(phoneNumRegex.findall(message)) #match object
print(mo.group())
