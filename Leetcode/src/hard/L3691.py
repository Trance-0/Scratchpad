class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        # do easy greedy
        na=sorted([(a,b) for a,b in enumerate(nums)],key=lambda x:x[1],reverse=True)
        # print(na)
        res=0
        n=len(nums)
        l,r=0,n-1 
        while k>0:
            dk=min(k,na[l][0]+(n-na[r][0]))
            res+=dk*(na[l][1]-na[r][1])
            if na[l+1][1]-na[l][1]<=na[r-1][1]-na[r][1]:
                l+=1
            else:
                r-=1
            k-=dk
        return res