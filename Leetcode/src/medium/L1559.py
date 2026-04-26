class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        # do a dfs to find if there is a cycle in the graph
        m,n=len(grid),len(grid[0])
        visited=[[False]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if visited[i][j]:
                    continue
                visited[i][j]=True
                stack=[(-1,-1,i,j)]
                while stack:
                    # print(visited,stack)
                    sx,sy,x,y=stack.pop()
                    for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                        nx,ny=x+dx,y+dy
                        if nx==sx and ny==sy:
                            continue
                        if 0<=nx<m and 0<=ny<n and grid[nx][ny]==grid[x][y]:
                            if visited[nx][ny]:
                                # print(grid[nx][ny],sx,sy,x,y,nx,ny,visited,stack)
                                return True
                            visited[nx][ny]=True
                            stack.append((x,y,nx,ny))
        return False