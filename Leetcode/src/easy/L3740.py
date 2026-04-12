class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        c=defaultdict(list)
        for i,e in enumerate(nums):
            c[e].append(i)
        res=float('inf')
        for k,v in c.items():
            for i in range(1,len(v)-1):
                res=min(res,v[i+1]-v[i-1])
        return -1 if res==float('inf') else res*2