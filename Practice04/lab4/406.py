a = int(input())


def f(a):
    n = 0
    m = 1
    for _ in range(0,a):
        yield n
        n,m = m,n+m
    




cmd = f(a)
first = True
for n in cmd:
    if first:
        print(n,end="")
        first = False
    else:
        print(f",{n}",end="")
