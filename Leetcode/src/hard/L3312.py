class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        # store pairs instead of actual vals.
        # cmp=list(Counter(nums).items())
        cm=collections.defaultdict(int)
        for i in nums:
            cm[i]+=1
        cmp=list(cm.items())
        n=len(cmp)
        print(n)
        bf=collections.defaultdict(int)
        for i in range(n):
            # add self pairs
            bf[cmp[i][0]] += cmp[i][1]*(cmp[i][1]-1)//2
            if i==n-1: break
            for j in range(i+1,n):
                bf[gcd(cmp[i][0], cmp[j][0])] += cmp[i][1] * cmp[j][1]
        st=sorted([(k,v) for k,v in bf.items() if v!=0], key=lambda x: x[0])
        m=len(st)
        # print(st)
        # make prefix sum
        for i in range(1,len(st)):
            st[i]=(st[i][0], st[i][1]+st[i-1][1])
        print(m)
        res=[]
        for q in queries:
            # find first element >= q
            idx=bisect_right(st, q, key=lambda x: x[0])-1
            # print(idx,q)
            if idx==-1:
                res.append(st[0][0])
            else:
                res.append(st[idx][0])
        return res