class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        # seems brute force?
        n=len(s)
        res=0
        # for i in range(n):
        #     for c in 'abcdefghijklmnopqrstuvwxyz':
        #         if c==s[i]:
        #             continue
        #         cs=s[:i]+c+s[i+1:]
        #         cnt=set()
        #         ck=0
        #         for j in cs:
        #             if j not in cnt and len(cnt)==k:
        #                 ck+=1
        #                 cnt.clear()
        #             cnt.add(j)
        #         if len(cnt)>0:
        #             ck+=1
        #         print(cs,ck)
        #         res=max(res,ck)
        # return res

        # change repeated characters to it's max d char.
        # count for last occurrence of each char
        # last_occ=[-1]*26
        # pre_far=[]
        # for i,e in enumerate(s):
        #     last_occ[ord(e)-ord('a')]=i
        #     pre_far.append(min([e,chr(ord('a')+i)] for i,e in enumerate(last_occ))[1])
        # last_occ=[n]*26
        # post_far=[]
        # for i in range(n-1,-1,-1):
        #     last_occ[ord(s[i])-ord('a')]=i
        #     post_far.append(max([e,chr(ord('a')+i)] for i,e in enumerate(last_occ))[1])
        # post_far=post_far[::-1]
        # res=0
        # for i in range(n):
        #     for c in [pre_far[i],post_far[i]]:
        #         if c==s[i]:
        #             continue
        #         cs=s[:i]+c+s[i+1:]
        #         cnt=set()
        #         ck=0
        #         for j in cs:
        #             if j not in cnt and len(cnt)==k:
        #                 ck+=1
        #                 cnt.clear()
        #             cnt.add(j)
        #         if len(cnt)>0:
        #             ck+=1
        #         print(cs,ck)
        #         res=max(res,ck)
        # return res

        # use bitmask dp, lol, too easy
        # batch masking
        msks=[1<<ord(c)-ord('a') for c in s]
        @lru_cache(None)
        def dp(i,can_change, mask):
            if i==n:
                return 0
            new_mask=msks[i]|mask
            ret=1+dp(i+1,can_change,msks[i]) if new_mask.bit_count()>k else dp(i+1,can_change,new_mask)
            if can_change:
                for j in range(26):
                    new_mask=(1<<j)|mask
                    ret=max(ret,1+dp(i+1,False,(1<<j)) if new_mask.bit_count()>k else dp(i+1,False,new_mask))
            return ret
        return dp(0,True,0)+1