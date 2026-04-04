class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        # easy dp
        m,n=len(coins),len(coins[0])
        opt=[[[0]*3 for _ in range(n)] for _ in range(m)]
        for k in range(3):
            for i in range(m):
                for j in range(n):
                    if i==0 and j==0:
                        opt[i][j][k]=coins[i][j]
                        if k>0:
                            opt[i][j][k]=max(coins[i][j],0)
                    elif i==0:
                        opt[i][j][k]=opt[i][j-1][k]+coins[i][j]
                        if k>0:
                            opt[i][j][k]=max(opt[i][j-1][k-1],opt[i][j][k])
                    elif j==0:
                        opt[i][j][k]=opt[i-1][j][k]+coins[i][j]
                        if k>0:
                            opt[i][j][k]=max(opt[i-1][j][k-1],opt[i][j][k])
                    else:
                        opt[i][j][k]=max(opt[i-1][j][k],opt[i][j-1][k])+coins[i][j]
                        if k>0:
                            opt[i][j][k]=max([opt[i-1][j][k-1],opt[i][j-1][k-1],opt[i][j][k]])
            # for p in opt:
            #     print([q[k] for q in p])
        return max(opt[-1][-1])