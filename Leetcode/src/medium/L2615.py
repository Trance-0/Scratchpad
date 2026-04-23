class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[0]*n
        count=defaultdict(list)
        for i,e in enumerate(nums):
            count[e].append(i)
        for _,v in count.items():
            s=sum([i-v[0] for i in v])
            for i,e in enumerate(v):
                res[e]=s
                if i+1<len(v):
                    s+=i*(v[i+1]-v[i])-(len(v)-1-i)*(v[i+1]-v[i])
        return res