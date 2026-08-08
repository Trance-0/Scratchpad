class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n=len(nums)
        pg=[]
        c=nums[0]
        for i in nums:
            c=max(c,i)
            pg.append(gcd(c,i))
        pg.sort()
        res=0
        for i in range(n//2):
            res+=gcd(pg[i],pg[n-i-1])
        if n%2==1:
            res+=pg[n//2]
        return res