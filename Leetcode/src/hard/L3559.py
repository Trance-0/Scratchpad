class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        # use 2dp? tree means unique path for each pair of nodes
        # the goal is to find common ancestor of 2 nodes, and assign weights to the two path to sum the possible values
        # refactor tree structures
        ## construct adjacent list
        adj=[[] for _ in range(len(edges)+1)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        ## construct parent list via bfs, assign depth to each node
        tr=[-1 for _ in range(len(edges)+1)]
        depth=[0 for _ in range(len(edges)+1)]
        q=deque([0])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if v!=tr[u]:
                    tr[v]=u
                    depth[v]=depth[u]+1
                    q.append(v)
        ## dfs to find common ancestor (path length) and assign weights
        @lru_cache(None)
        def dfs(i,j):
            if i==j:
                return 0
            # always reduce depth of the deeper node
            if depth[i]>depth[j]:
                return dfs(tr[i],j)+1
            elif depth[i]<depth[j]:
                return dfs(i,tr[j])+1
            else:
                return dfs(tr[i],tr[j])+2
        res=[]
        # precompute ways to assign weights for path of given length for
        dp=[0,1]
        MOD=10**9+7
        for i in range(2,max(depth)*2+1):
            dp.append(dp[-1]*2%MOD)
        for a,b in queries:
            res.append(dfs(a,b))
        return res