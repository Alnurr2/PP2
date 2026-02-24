N = int(input(""))

def smth(N):
    cnt = 0
    while cnt <= N:
        yield cnt
        cnt+=1


cmd = smth(N)
for n in cmd:
    if n % 12 == 0:
        print(n, end= " ")

