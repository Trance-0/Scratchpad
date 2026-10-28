class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        # a case by case, among all the remainders, sliding window to keep count, eg 2*2 mod 3 == 1
        n=len(nums)
        nums=[x%k for x in nums]
        # first, let's do legacy dp, maybe we can compute the pairs first?
        mp=defaultdict(list)
        for i in range(1,k):
            for j in range(1,k):
                mp[(i*j)%k].append((i,j))
        dp=[[0]*k for _ in range(n)]
        # dp[i][j] denote the number of subarrays ending at index i with product % k == j
        for i in range(n):
            # select nothing
            dp[i][nums[i]]+=1
            if i!=0:
                for j in range(k):
                    dp[i][(j*nums[i])%k]+=dp[i-1][j]
        # solve for the ways to build the subarray product
        return [sum([dp[i][k] for i in range(n)]) for j in range(n)]