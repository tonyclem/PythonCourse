import re

pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
pattern2 = re.compile(r"[A-Za-z0-9$%#@]{8,}\d")
string = 'Clement'
password = 'hlgjlnj553kl%8'

a = pattern.search(string)
check = pattern2.fullmatch(password)
print(check)
