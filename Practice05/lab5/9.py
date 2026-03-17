import re

S = input("")
x =re.findall(r"\b\w{3}\b",S)


print(len(x))

