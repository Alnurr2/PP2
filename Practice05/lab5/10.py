import re

S = input("")
x =re.findall(r"dog|cat",S)



if len(x) == 0:
    print("No")
else:
    print("Yes")

