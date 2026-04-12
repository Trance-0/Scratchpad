class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        # Hope you will not see the hard ver tomorrow.
        M=10**9+7
        for l,r,k,v in queries:
            for i in range(l,r+1,k):
                nums[i]=(nums[i]*v)%M
        return reduce(lambda x,y:x^y,nums)