class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n=len(nums)
        cur=sum([i*nums[i] for i in range(n)])
        s=sum(nums)
        res=0
        for i in range(n-1):
            cur+=(n-1)*nums[i]-s
            res=max(res,cur)
        return res