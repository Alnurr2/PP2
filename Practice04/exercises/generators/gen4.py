a,b = map(int,input().split())

def squares(a,b):
    first = a
    while first <= b:
        yield first**2
        first +=1


cmd = squares(a,b)
for n in cmd:
    print(n)

