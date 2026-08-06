from typing import List
from functools import lru_cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        @lru_cache(None)
        def take(h,t,a):
            if h==t:
                return (piles[h],0) if a else (0,piles[h])
            # best for a,b
            ha,hb=take(h+1,t,not a)
            ta,tb=take(h,t-1,not a)
            if a:
                if ha+piles[h]>ta+piles[t]:
                    return ha+piles[h],hb
                else:
                    return ta+piles[t],tb
            else:
                if hb+piles[h]>tb+piles[t]:
                    return ha,hb+piles[h]
                else:
                    return ta,tb+piles[h]
        n=len(piles)
        a,b=take(0,n-1,True)
        return a>b
    
if __name__ == "__main__":
    s = Solution()
    print(s.stoneGame([5,3,4,5]))  # Output: True
    print(s.stoneGame([3,7,2,3]))  # Output: True
    print(s.stoneGame([1,7,7,1]))  # Output: False
    print(s.stoneGame([1,2,3,4,5,6]))  # Output: True