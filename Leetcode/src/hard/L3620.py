class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        # binary search with bfs
        # preprocess adj list
        n=len(online)
        adj=collections.defaultdict(list)
        for a,b,e in edges:
            if not online[a] or not online[b]:
                continue
            adj[a].append((b,e))
        def canPass(mx):
            # conditional dijkstra, only consider edges with mx<=e
            d=[float('inf')]*n
            d[0]=0
            pq=[(0,0)]
            while pq:
                # current node and current distance
                cd,c=heappop(pq)
                # remove stale edge updates
                if cd>d[c]:
                    continue
                for nx,nw in adj[c]:
                    # update better edges
                    if d[nx]<=nw+cd or nw<mx:
                        continue
                    d[nx]=nw+cd     
                    # debug
                    # print(nx,nw+cd)
                    heappush(pq,(nw+cd,nx))
            # check if we can reach any online node within k distance
            if d[-1]<=k:
                return True
            return False
        if not canPass(0):
            return -1
        l,h=0,max([e for _,_,e in edges])+1
        while l<h:
            m=(l+h)//2
            if canPass(m):
                l=m+1
            else:
                h=m
        return l-1