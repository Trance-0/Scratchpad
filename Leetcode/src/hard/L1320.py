class Solution:
    def minimumDistance(self, word: str) -> int:
        board=[
            [0,1,2,3,4,5],
            [6,7,8,9,10,11],
            [12,13,14,15,16,17],
            [18,19,20,21,22,23],
            [24,25]
        ]
        d=[[0]*26 for _ in range(26)]
        for y1 in range(5):
            for x1 in range(6):
                if y1==4 and x1>1:
                    break
                for y2 in range(5):
                    for x2 in range(6):
                        if y2==4 and x2>1:
                            break
                        d[board[y1][x1]][board[y2][x2]]=abs(y1-y2)+abs(x1-x2)
        c=[ord(i)-ord('A') for i in word]
        @lru_cache(None)
        def dp(i,a,b):
            if i==len(c):
                return 0
            # move left
            if a>-1:
                res=dp(i+1,c[i],b)+d[a][c[i]]
            else:
                res=dp(i+1,c[i],b)
            # move right
            if b>-1:
                res=min(res,dp(i+1,a,c[i])+d[b][c[i]])
            else:
                res=min(res,dp(i+1,a,c[i]))
            return res
        return dp(0,-1,-1)