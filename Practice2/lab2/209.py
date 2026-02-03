mx = -10000000000
mn = 1000000000
n = int(input(""))
m = input("")
m = m.split()
intlist = list(map(int,m))


for i in range(len(intlist)):
    if intlist[i] > mx:
        mx = intlist[i]
    else:
        continue

for i in range(len(intlist)):
    if intlist[i] <  mn:
        mn = intlist[i]
    else:
        continue

for i in range(len(intlist)):
    if intlist[i] ==  mx:
        print(mn,end=" ")
    else:
        print(intlist[i], end=" ")


