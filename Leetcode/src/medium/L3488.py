class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        c=collections.defaultdict(list)
        n=len(nums)
        for i,e in enumerate(nums):
            c[e].append(i)
        res=[]
        for k in queries:
            if nums[k] not in c or len(c[nums[k]])<2:
                res.append(-1)
                continue
            a=c[nums[k]]
            idx=bisect.bisect_left(a,k)
            # print(idx,len(a))
            if idx==0:
                res.append(min(n-a[-1]+a[0],a[idx+1]-k))
            elif idx==len(c[nums[k]])-1:
                res.append(min(n-a[-1]+a[0],k-a[idx-1]))
            else:
                res.append(min(a[idx+1]-k,k-a[idx-1]))
        return res