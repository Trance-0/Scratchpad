class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m,n=len(grid),len(grid[0])
        l,r=collections.defaultdict(int),collections.defaultdict(int)
        ls,rs=0,0
        def conn(a,b,c,d,ele):
            # if any one-liner, then you can only cut from boarder
            if a==c:
                if (ele==grid[a][b] or ele==grid[a][d]):
                    return True
                return False
            if b==d:
                if (ele==grid[a][b] or ele==grid[c][b]):
                    return True
                return False
            return True
        for i in range(m):
            for j in range(n):
                r[grid[i][j]]+=1
                rs+=grid[i][j]
        for i in range(m):
            for j in range(n):
                l[grid[i][j]]+=1
                ls+=grid[i][j]
                rs-=grid[i][j]
                r[grid[i][j]]-=1
            if ls==rs:
                return True
            if ls<rs and rs-ls in r and r[rs-ls]>0 and conn(i+1,0,m-1,n-1,rs-ls):
                return True
            if rs<ls and ls-rs in l and l[ls-rs]>0 and conn(0,0,i,n-1,ls-rs):
                return True
        l,r=collections.defaultdict(int),collections.defaultdict(int)
        ls,rs=0,0
        for i in range(m):
            for j in range(n):
                r[grid[i][j]]+=1
                rs+=grid[i][j]
        for j in range(n):
            for i in range(m):
                l[grid[i][j]]+=1
                ls+=grid[i][j]
                rs-=grid[i][j]
                r[grid[i][j]]-=1
            if ls==rs:
                return True
            if ls<rs and rs-ls in r and r[rs-ls]>0 and conn(0,j+1,m-1,n-1,rs-ls):
                return True
            if rs<ls and ls-rs in l and l[ls-rs]>0 and conn(0,0,m-1,j,ls-rs):
                return True
        return False