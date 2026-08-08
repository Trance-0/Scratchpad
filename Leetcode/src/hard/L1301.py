class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        # dijk with eq
        # graph construct
        m, n = len(board), len(board[0])
        adj = collections.defaultdict(list)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] not in "SXE":
                        adj[(i, j)].append((ni, nj))