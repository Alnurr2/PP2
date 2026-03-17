import re

S = input("")
x =re.search(r"\S+[@]+\S+[.]+\S+",S)


if x is None:
    print("No email")
else:
    print(x.group())