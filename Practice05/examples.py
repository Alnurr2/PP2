import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)


print(x)


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())


import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)

import re

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)



import re

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print(x)



import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())


txt = "hello planet"

x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")