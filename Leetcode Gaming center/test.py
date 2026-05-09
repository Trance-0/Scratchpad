
def constructDistancedSequence(n: int):
    rn=2*(n-1)+1
    res=[-1]*rn
    tot=[]
    def put_digit(a):
        if a==1:
            for i in range(rn):
                if res[i]==-1:
                    res[i]=1
                    tot.append([i for i in res])
                    res[i]=-1
        for i in range(rn-a):
            if res[i]==-1 and res[i+a]==-1:
                res[i]=a
                res[i+a]=a
                # print(res)
                if put_digit(a-1): return True
                res[i]=-1
                res[i+a]=-1
        return False
    put_digit(n)
    return max(tot)

for i in range(1,21):
    print(constructDistancedSequence(i))
