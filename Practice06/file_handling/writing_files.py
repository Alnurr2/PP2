with open("welcome.txt", "a") as f:
  f.write("Now the file has more content!")

with open("welcome.txt", "w") as f:
  f.write("Woops! I have deleted the content!")

with open("welcome.txt", "a") as f:
  f.write("Now the file has more content!")

with open("welcome.txt", "w") as f:
  f.write("Woops! I have deleted the content!")