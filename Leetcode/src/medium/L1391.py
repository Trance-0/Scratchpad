class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        street=[((0,-1),(0,1)),((-1,0),(1,0)),((1,0),(0,-1)),((1,0),(0,1)),((-1,0),(0,-1)),((-1,0),(0,1))]
        m,n=len(grid),len(grid[0])
        visited=[[False]*n for _ in range(m)]
        def dfs(px,py,x,y):
            print(x,y)
            if x==m-1 and y==n-1:
                return True
            if visited[x][y]:
                return False
            visited[x][y]=True
            dx,dy=street[grid[x][y]-1][0]
            if x+dx!=px and y+dy!=py and 0<=x+dx<m and 0<=y+dy<n and (dx,dy) in street[grid[x+dx][y+dy]-1] and dfs(x,y,x+dx,y+dy):
                return True
            dx,dy=street[grid[x][y]-1][1]
            if  x+dx!=px and y+dy!=py and 0<=x+dx<m and 0<=y+dy<n and (dx,dy) in street[grid[x+dx][y+dy]-1]  and dfs(x,y,x+dx,y+dy):
                return True
            return False
        return dfs(-1,-1,0,0)