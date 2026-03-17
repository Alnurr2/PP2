import re

S = input("")
P = input("")
x =re.search(P,S)

if x is None:
    print("No")
else:
    print("Yes")