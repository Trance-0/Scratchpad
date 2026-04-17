class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        c=defaultdict(list)
        nums=[str(i) for i in nums]
        for i,e in enumerate(nums):
            c[e].append(i)
        res=float('inf')
        for k,v in c.items():
            l=k[::-1]
            # remove leading zeros
            while l and l[0]=='0':
                l.pop(0)
            print(l,k)
            if l==k:
                for i in range(len(v)-1):
                    res=min(res,v[i+1]-v[i])
                continue
            if l not in c:
                continue
            for cv in v:
                print(c[l],v)
                idx=bisect.bisect_left(c[l],cv)
                if idx<len(c[l])-1:
                    res=min(res,abs(c[l][idx+1]-cv))
                if idx<len(c[l]):
                    res=min(res,abs(c[l][idx]-cv))
        return -1 if res==float('inf') else res