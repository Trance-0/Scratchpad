class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for i in range(y,y+k):
            for j in range(k//2):
                grid[x+j][i],grid[x+k-1-j][i]=grid[x+k-1-j][i],grid[x+j][i]
        return grid