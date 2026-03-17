import re

S = input("")
x =re.compile(r"^\d+$")
p = x.search(S)


if p is  None:
    print("No match")
else:
    print("Match")



