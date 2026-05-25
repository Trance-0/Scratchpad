class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # parse for easy operations
        a=[i=='0' for i in s]
        if not a[-1]: return False
        # easy dual pointer, note that only jump forward is possible
        # print(a)
        l=0
        for h,e in enumerate(a):
            if not e or h==0: continue
            while l<h-maxJump or not a[l]:
                l+=1
            # label as impossible to solve, note l==h at most.
            if l>h-minJump:
                a[h]=False
            # print(a,h,l,e)
        return a[-1]