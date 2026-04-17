class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        l,r=start,start
        while nums[l]!= target and nums[r]!=target:
            if l>0:
                l-=1
            if r<len(nums)-1:
                r+=1
        return max(abs(l-start),abs(r-start))