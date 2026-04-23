class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        res=[]
        for q in queries:
            for d in dictionary:
                cnt=0
                for i in range(len(q)):
                    if q[i]!=d[i]:
                        cnt+=1
                        if cnt>2:
                            break
                if cnt<=2:
                    res.append(q)
                    break
        return res