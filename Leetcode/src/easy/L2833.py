class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        d=0
        c=0
        for i in moves:
            if i=='R':
                c-=1
            elif i=='L':
                c+=1
            else:
                d+=1
        return abs(c)+d