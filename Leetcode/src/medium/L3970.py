import heapq
from typing import List

class Solution:
    def shortestPath(
        self, n: int, edges: List[List[int]], labels: str, k: int
    ) -> int:
        if k <= 0:
            return -1

        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        # cnt = consecutive same-label nodes minus one
        d = [[float("inf")] * k for _ in range(n)]
        d[0][0] = 0

        # (distance, current node, cnt)
        q = [(0, 0, 0)]

        while q:
            dist, u, cnt = heapq.heappop(q)

            if dist != d[u][cnt]:
                continue

            if u == n - 1:
                return dist

            for v, w in adj[u]:
                ncnt = cnt + 1 if labels[v] == labels[u] else 0
                if ncnt >= k:
                    continue

                ndist = dist + w
                if ndist < d[v][ncnt]:
                    d[v][ncnt] = ndist
                    heapq.heappush(q, (ndist, v, ncnt))

        return -1