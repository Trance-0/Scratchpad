class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        # reverse union find
        parent=[i for i in range(c)]
        min_value=[c+1 for i in range(c)]
        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        def union(x,y):
            # set parent of y to x, require x is on.
            # print(f'merge{x}:{y}')
            x=find(x)
            y=find(y)
            if x!=y:
                # print(f'setp[{y}] to {x}')
                parent[y]=x
                min_value[x]=min(min_value[x],min_value[y])
        on=[0]*c
        for code,i in queries:
            if code==2:
                on[i-1]+=1
        # connect initial 
        adj=[[] for _ in range(c)]
        for a,b in connections:
            adj[a-1].append(b-1)
            adj[b-1].append(a-1)
        for i in range(c):
            if on[i]==0:
                min_value[find(i)]=min(min_value[find(i)],i)
            for j in adj[i]:
                union(i,j)
        result=[]
        for code,i in queries[::-1]:
            i-=1
            if code==1:
                print(min_value,parent,on,i)
                if on[i]==0:
                    result.append(i+1)
                else:
                    val=min_value[find(i)]
                    print(val,i)
                    result.append(val+1 if val!=c+1 else -1)
            else:
                on[i]-=1
                if on[i]==0:
                    min_value[find(i)]=min(min_value[find(i)],i)
        return result[::-1]
