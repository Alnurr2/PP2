S= input("")

class Reverse:
    def __init__(self,S):
        self.S = S
        self.index = len(S)
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -=1
            return self.S[self.index]
    

rev = Reverse(S)

Sr = iter(rev)

for l in Sr:
    print(l,end="")