class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        # dp, move down or right
        m, n = len(grid), len(grid[0])
        @lru_cache(None)
        def hasPath(a,i,j):
            # return a+i+j==0 or (i-1>=0 and hasPath(a+1 if grid[i-1][j]==')' else a-1,i-1,j)) or (j-1>=0 and hasPath(a+1 if grid[i][j-1]==')' else a-1,i,j-1))
            if a+i+j==0:
                return True
            if i-1>=0:
                if grid[i-1][j]==')':
                    if hasPath(a+1,i-1,j):
                        return True
                else:
                    if a>0 and hasPath(a-1,i-1,j):
                        return True
            if j-1>=0:
                if grid[i][j-1]==')':
                    if hasPath(a+1,i,j-1):
                        return True
                else:
                    if a>0 and hasPath(a-1,i,j-1):
                        return True
            return False
        return grid[m-1][n-1]==')' and hasPath(1,m-1,n-1)