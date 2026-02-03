n = int(input(""))
m = input("")
m = m.split()
intlist = list(map(int,m))

for i in range(len(intlist)):
    print(intlist[i]**2,end=" ")

