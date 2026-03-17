import re

S = input("")
P = input("")
y = re.escape(P)
x =re.findall(y,S)


print(len(x))

