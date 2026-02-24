n = int(input(""))
cnt = 0
def prime(n):
    for num in range(1,n+1):
        if num < 2:
            continue
        isit = True    
        for i in range(2,n):
            if num%i == 0:
                isit = False
                break
            if isit:
                yield num
             
    


for j in prime(n):
    print(j,end=" ")