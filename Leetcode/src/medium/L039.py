class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        # brute force
        n = len(values)
        @lru_cache(None)
        def dfs(i, j):
            if i + 2 > j:
                return 0
            if i + 2 == j:
                return values[i] * values[j] * values[i+1]
            result = float('inf')
            for k in range(i + 1, j):
                result = min(result, dfs(i, k) + dfs(k, j)+values[i] * values[k] * values[j])
            return result
        return dfs(0, n-1)





