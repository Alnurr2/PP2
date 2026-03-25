#open and read the file after the overwriting:
with open("welcome.txt") as f:
  print(f.read())


with open("welcome.txt", "a") as f:
  f.write("Now the file has more content!")


#open and read the file after the appending:
with open("welcome.txt") as f:
  print(f.read())


with open("welcome.txt", "w") as f:
  f.write("Woops! I have deleted the content!")


#open and read the file after the overwriting:
with open("welcome.txt") as f:
  print(f.read())

