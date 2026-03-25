f = open("welcome.txt")
print(f.read())

with open("welcome.txt") as f:
  print(f.read())

f = open("welcome.txt")
print(f.readline())
f.close()


with open("welcome.txt") as f:
  print(f.read(5))


with open("welcome.txt") as f:
  print(f.readline())


with open("welcome.txt") as f:
  print(f.readline())
  print(f.readline())

with open("welcome.txt") as f:
  for x in f:
    print(x)
