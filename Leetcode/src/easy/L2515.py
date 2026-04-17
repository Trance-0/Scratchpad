class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        if words[startIndex]==target:
            return 0
        l,r=startIndex,startIndex
        n=len(words)
        d=0
        while d==0 or l!=r:
            d+=1
            l=(l+n-1)%n
            r=(r+1)%n
            print(words[l],words[r],target)
            if words[l]==target or words[r]==target:
                return d
        return -1