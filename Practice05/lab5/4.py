import re

S = input("")
x =re.findall(r"\d",S)

print(*x,sep=" ")

