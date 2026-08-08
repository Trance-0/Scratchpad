class Solution:
    def find(self, p: List[int], x: int) -> int:
        if p[x] != x:
            p[x] = self.find(p, p[x])
        return p[x]

    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        # disjoint sets
        p = [i for i in range(n)]
        for i in range(n-1):
            j = i + 1
            if abs(nums[i] - nums[j]) <= maxDiff:
                p[self.find(p, j)] = self.find(p, i)

        # answer queries
        res = []
        for x, y in queries:
            res.append(self.find(p, x) == self.find(p, y))
        return res