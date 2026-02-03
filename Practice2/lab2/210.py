cnt = 0
n = int(input(""))
m = input("")
m = m.split()
intlist = list(map(int,m))

sorti = sorted(intlist,reverse=True)

print(*sorti)
