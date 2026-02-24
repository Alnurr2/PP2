a = int(input())

def cntdwn(a):
    while a!=-1:
        yield a
        a -=1


cmd = cntdwn(a)
for n in cmd:
    print(n)

