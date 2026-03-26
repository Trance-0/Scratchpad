class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n,m=len(skill),len(mana)
        init=[0]*(n+1)
        for i in range(m):
            for j in range(n):
                init[j+1]=max(init[j+1],init[j])+skill[j]*mana[i]
            for j in range(n-1,0,-1):
                init[j]=init[j+1]-skill[j]*mana[i]
        return init[-1]