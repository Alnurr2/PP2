sum = 0
n = int(input(""))
m = input("")
m = m.split()
intlist = list(map(int,m))

for i in range(len(intlist)):
    sum+=intlist[i]

print(sum)
