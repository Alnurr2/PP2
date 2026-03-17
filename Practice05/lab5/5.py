import re

S = input("")
x =re.findall(r"^\w+\d$",S)

if len(x) == 1:
    print("Yes")
else:
    print("No")

