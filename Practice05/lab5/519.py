import re

S = input("")
x =re.compile(r"\b\w+\b")
p = x.findall(S)

print(len(p))





