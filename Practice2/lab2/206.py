mx = -10000000000
mx_i = 0
n = int(input(""))
m = input("")
m = m.split()
intlist = list(map(int,m))


for i in range(len(intlist)):
    if intlist[i] > mx:
        mx = intlist[i]
        mx_i = i
    else:
        continue


print(mx_i+1)

