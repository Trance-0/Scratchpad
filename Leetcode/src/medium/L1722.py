class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        # disjoint set
        n=len(source)
        parent=[i for i in range(n)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            parent[find(x)]=find(y)
        for x,y in allowedSwaps:
            union(x,y)
        index_group=defaultdict(list)
        for i in range(n):
            index_group[find(i)].append(i)
        print(index_group)
        res=0
        for _,v in index_group.items():
            c=defaultdict(int)
            for i in v:
                c[source[i]]+=1
                c[target[i]]-=1
            for cnt in c.values():
                res+=abs(cnt)
        return res//2