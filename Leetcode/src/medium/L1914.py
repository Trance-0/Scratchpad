class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n=len(grid),len(grid[0])
        l,r,d,u=0,n-1,0,m-1
        while l<r and d<u:
            buf=[]
            for i in range(d,u):
                buf.append(grid[i][l])
            for i in range(l,r):
                buf.append(grid[u][i])
            for i in range(u,d,-1):
                buf.append(grid[i][r])
            for i in range(r,l,-1):
                buf.append(grid[d][i])
            print(buf)
            buf=buf[-k%len(buf):]+buf[:-k%len(buf)]
            for i in range(d,u):
                grid[i][l]=buf.pop(0)
            for i in range(l,r):
                grid[u][i]=buf.pop(0)
            for i in range(u,d,-1):
                grid[i][r]=buf.pop(0)
            for i in range(r,l,-1):
                grid[d][i]=buf.pop(0)
            l+=1;r-=1;d+=1;u-=1
        return grid