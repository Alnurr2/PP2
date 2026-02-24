N = int(input(""))

def smth(N):
    cnt = 0
    while cnt <= N:
        yield cnt
        cnt+=2

first = True
cmd = smth(N)
for n in cmd:
    if first:
        print(n,end="")
        first = False
    else:
        print(f",{n}",end="")
