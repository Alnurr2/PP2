import re

f = input("")
x =re.match(r"Hello",f)

if x == None:
    print("No")
else:
    print("Yes")