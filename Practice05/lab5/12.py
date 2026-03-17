import re

S = input("")
x =re.findall(r"\d{2,}",S)




print(*x,sep=" ")



