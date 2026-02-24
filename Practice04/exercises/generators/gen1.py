N = int(input(""))

def smth(N):
    cnt = 0
    while cnt < N:
        cnt+=1
        yield cnt**2

cmd = smth(N)
for n in cmd:
    print(n)









