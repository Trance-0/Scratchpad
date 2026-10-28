class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # brute force, check all possible xor values and return the minimum cost
        m,n=len(grid),len(grid[0])
        @lru_cache(None)
        def dfs(i,j,cost):
            if i==m-1 and j==n-1:
                return cost
            if i==m-1:
                return dfs(i,j+1,cost^grid[i][j])
            if j==n-1:
                return dfs(i+1,j,cost^grid[i][j])
            return min(dfs(i,j+1,cost^grid[i][j]),dfs(i+1,j,cost^grid[i][j]))
        return dfs(0,0,0)