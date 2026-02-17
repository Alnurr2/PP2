s = input("")
T = False

def valid(s,T):
    for d in s:
        if int(d) % 2 == 0:
            T = True
        else:
            T = False
            break
        
        
    return T



if valid(s,T) == True:
    print("Valid")
else:
    print("Not valid")