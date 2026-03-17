import re

S = input("")
x =re.sub(S,S,S)
y = re.findall(r"\d+",S)
n = str(y)
for k in n:
        print(k*2,sep = "")