import re

string = 'search inside of this text please!'
a = re.search('this', string)
print(a.span())
print(a.start())
print(a.group())
