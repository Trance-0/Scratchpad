class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m,n=len(grid),len(grid[0])
        dp=None

        for rem in range(k+1):
            dpn=[[-1]*n for _ in range(m)]
            for i in range(m-1,-1,-1):
                for j in range(n-1,-1,-1):
                    if i==m-1 and j==n-1:
                        if grid[i][j]>0:
                            if rem>0:
                                dpn[i][j]=grid[i][j]
                        else:
                            dpn[i][j]=0
                        continue

                    if rem==0:
                        if grid[i][j]>0:
                            continue
                        a=dpn[i+1][j] if i+1<m else -1
                        b=dpn[i][j+1] if j+1<n else -1
                        if a==-1 and b==-1:
                            continue
                        if a==-1:
                            dpn[i][j]=b+grid[i][j]
                        elif b==-1:
                            dpn[i][j]=a+grid[i][j]
                        else:
                            dpn[i][j]=max(a,b)+grid[i][j]
                    else:
                        if grid[i][j]>0:
                            a=dp[i+1][j] if i+1<m else -1
                            b=dp[i][j+1] if j+1<n else -1
                            if a==-1 and b==-1:
                                continue
                            if a==-1:
                                dpn[i][j]=b+grid[i][j]
                            elif b==-1:
                                dpn[i][j]=a+grid[i][j]
                            else:
                                dpn[i][j]=max(a,b)+grid[i][j]
                        else:
                            a=dpn[i+1][j] if i+1<m else -1
                            b=dpn[i][j+1] if j+1<n else -1
                            dpn[i][j]=max(a,b)
            dp=dpn

        return dp[0][0]
