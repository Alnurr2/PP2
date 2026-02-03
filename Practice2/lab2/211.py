n = int(input(""))
m = input("")
m = m.split()
intlist = list(map(int,m))

for i in range(len(intlist)):
    if intlist[i] > 0:
        cnt+=1
    else:
        continue

print(cnt)
