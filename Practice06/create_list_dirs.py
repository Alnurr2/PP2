import shutil



with open("welcome.txt","r") as file:
    data = file.read()
    copying = shutil.copy(r"welcome.txt",'destination.txt')
    print("Content has copied.")


# automatic closing
with open("welcome.txt","r") as file:
    data = file.read()
    print(data)

with open("welcome.txt","a") as file:
    file.write("New line content ")

with open("welcome.txt","r") as file:
    data = file.read()
    print(data)


