class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # binary search for max valid distance
        # a monotonic increasing function
        n=len(points)
        sides=[[],[],[],[]]
        for a,b in points:
            if b==0:
                sides[0].append((a,b))
            elif a==side:
                sides[1].append((a,b))
            elif b==side:
                sides[2].append((a,b))
            else:
                sides[3].append((a,b))
        # compute the distance
        sides[0].sort(key=lambda x:x[0])
        sides[1].sort(key=lambda x:x[1])
        sides[2].sort(key=lambda x:x[0],reverse=True)
        sides[3].sort(key=lambda x:x[1],reverse=True)
        # print(sides)
        prev=[-1,-1]
        start=[]
        d=[]
        for s in sides:
            for a,b in s:
                if prev[0]==-1:
                    prev=(a,b)
                    start=(a,b)
                    continue
                d.append(abs(prev[0]-a)+abs(prev[1]-b))
                prev=(a,b)
        d.append(abs(prev[0]-start[0])+abs(prev[1]-start[1]))
        p=[0]
        for i in d[:-1]:
            p.append(p[-1]+i)
        print(d,p)
        def select(mindist):
            nonlocal p
            # binary search for greedy picking, starting at i, what is the max valid cycles
            # mx store, what is the maximum index of point you can select if you want to keep p[i] as root
            mx=[0]*n
            for i in range(n):
                target=(p[i]+mindist)%(side*4)
                idx=bisect.bisect_left(p,target)
                print(target,idx)
                mx[i]=idx%n
            # literative cycle detection
            print(mindist,mx)
            # record ending points and cycle length
            v=[(-1,-1)]*n
            res=0
            for start in range(n):
                if v[start][0]!=-1:
                    continue
                v[start]=True
                cur=mx[start]
                print("start",start,cur,mindist,abs(p[start]-p[cur]),side*4-abs(p[start]-p[cur]))
                cycle=1
                # od=[start,cur]
                # any time should not fall in to the first edge region
                # while min(abs(p[start]-p[cur]),side*4-abs(p[start]-p[cur]))>=mindist:
                #     v[cur]=True
                #     cur=mx[cur]
                #     cycle+=1
                #     od.append(cur)
                #     print(mindist,start,cur,cycle)
                #     if v[cur][0]!=-1:
                #         # test if we can add more edge
                #         ending, remains=v[cur]
                #         if side*4-abs(p[ending]-p[remains])>=mindist:
                #             cycle+=1
                #         cycle
                #         break
                res=max(res,cycle)
            return res

        # binary search for max valid distance
        l,r=0,side*4
        while l<r:
            mid=(l+r)//2
            if select(mid)<k:
                r=mid
            else:
                l=mid+1
        return l-1