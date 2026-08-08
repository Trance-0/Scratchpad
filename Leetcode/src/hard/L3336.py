from typing import List
from collections import defaultdict
from math import gcd


class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        # categorized all sequence by gcd?, then count disjoint segments in each group with combint
        # n=len(nums)
        # d=defaultdict(list)
        # for l in range(n):
        #     g = nums[l]
        #     for r in range(l, n):
        #         g = gcd(g, nums[r])
        #         d[g].append((l, r))
        # # count disjoint segments in each group
        # res = 0
        # for l in d.values():
        #     # l sort by start, r sort by end
        #     r=sorted(l, key=lambda x: x[1])
        #     cn = len(l)
        #     # count disjoint segments
        #     cnt = 0
        #     li = 0
        #     for ri in range(cn):
        #         while li < cn and r[ri][1] >= l[li][0]:
        #             li += 1
        #         if li >= cn or r[ri][1] < l[li][0]:
        #             break
        #         cnt = (cnt + cn - li+1) % (10**9 + 7)
        #         print (r[ri], l[li],cn - li+1)
        #     res = (res + cnt) % (10**9 + 7)
        #     print (l, r, cnt)
        # return res % (10**9 + 7)
        # sub sequence is 2**n
        # H1: Use dynamic programming to store number of subsequences up till index i with GCD g1 and g2. 