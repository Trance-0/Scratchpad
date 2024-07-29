def floydWarshall(edges,n,inf:int=10**9,is_bidirectional:bool=False):
    # return minDistance of all node in range n given edges
    minD=[[0 if i==j else inf for i in range(n)] for j in range(n)]
    for a,b,w in edges:
        minD[a][b]=min(minD[a][b],w)
        if is_bidirectional: minD[b][a]=min(minD[a][b],w)
    for k in range(n):
        for a in range(n):
            if a==k: continue
            for b in range(n):
                if a==b or b==k: continue
                minD[a][b]=min(minD[a][b],minD[a][k]+minD[k][b])
    return minD