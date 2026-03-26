class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n=len(grid)
        m=len(grid[0])
        arr=[0]*n
        for i in range(n):
            for j in range(m):
                arr[i]|=grid[i][j]
        return arr==[arr[-1]]*n