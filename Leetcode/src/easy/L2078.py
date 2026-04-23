class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        c=defaultdict(list)
        for i,e in enumerate(colors):
            c[e].append(i)
        res=0
        for k,v in c.items():
            for k2,v2 in c.items():
                if k!=k2:
                    res=max(res,abs(v[0]-v2[-1]),abs(v[-1]-v2[0]))
        return res