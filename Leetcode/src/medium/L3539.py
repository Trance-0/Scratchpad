from collections import Counter, defaultdict
from typing import List, Optional
import heapq
import bisect
import itertools
import math


class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        M=10**9+7
        c=Counter(nums)
        cl=list(c.items())
        n=len(cl)
        @lru_cache(None)
        def countSum(idx,srem,brem):
            # remaining sequence points and remaining bit points
            if idx==n and srem==0 and brem==0:
                return 1
            if brem