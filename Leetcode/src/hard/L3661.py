class Solution:
    def maxWalls(self, robots: List[int], distance: List[int], walls: List[int]) -> int:
        # dp, check if the robot shoot left or right on fixed indices
        n,m=len(robots),len(walls)
        rd=sorted(zip(robots,distance))
        walls.sort()
        print(rd,walls)
        # clear out the equal walls
        res=0
        i,j=0,0
        while i<n and j<m:
            if rd[i][0]==walls[j]:
                res+=1
                i+=1
                j+=1
            elif rd[i][0]<walls[j]:
                i+=1
            else:
                j+=1
        print(res)
        # 2dp, one for shooting left, one for shooting right for each robot, we dont' count the walls that are on the robots,
        optl=[[0]*2 for _ in range(n)]
        for i in range(n):
             # previous robot shoot left, current shoot left
            l1=bisect.bisect_left(walls,max(0 if i==0 else rd[i-1][0],rd[i][0]-rd[i][1]))
            # previous robot shoot right, current shoot left
            l2=bisect.bisect_left(walls,max(0 if i==0 else min(rd[i][0],rd[i-1][0]+rd[i-1][1]+1),rd[i][0]-rd[i][1]))
            # previous robot shoot rights, current shoot right
            r=bisect.bisect_right(walls,min(walls[-1] if i==n-1 else rd[i+1][0],rd[i][0]+rd[i][1]))
            # if i<n-1 and r<m and walls[r]==robots[i+1]:
            #     r-=1
            ml=bisect.bisect_left(walls,rd[i][0])
            mr=bisect.bisect_left(walls,rd[i][0]+1)
            print((ml-l1), (ml-l2), (r-mr),[l1,l2,ml,mr,r],robots[i])
            optl[i][0]=max((0 if i==0 else optl[i-1][0])+(ml-l1),(0 if i==0 else optl[i-1][1])+(ml-l2))
            optl[i][1]=(0 if i==0 else optl[i-1][0])+(r-mr)
            # print(optl[i])
        return max(optl[-1])+res