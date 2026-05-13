class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        # use difference array
        da=[0]*(limit*2+2)
        n=len(nums)
        for i in range(n//2):
            a,b=nums[i],nums[n-1-i]
            # 0 changes
            da[a+b]-=1
            da[a+b+1]+=1
            # 1 change
            da[min(a,b)+1]-=1
            da[max(a,b)+limit+1]+=1
            # 2 changes
            da[2]+=2
            da[limit*2+1]-=2
        res,c=n,0
        for i in range(2,limit*2+1):
            c+=da[i]
            # print(i,c)
            res=min(res,c)
        return res