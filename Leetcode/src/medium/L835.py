class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        max_overlap = 0

        def count_overlap(x_shift, y_shift):
            overlap = 0
            for i in range(n):
                for j in range(n):
                    if 0 <= i + x_shift < n and 0 <= j + y_shift < n:
                        overlap += img1[i][j] & img2[i + x_shift][j + y_shift]
            return overlap

        for x_shift in range(-n + 1, n):
            for y_shift in range(-n + 1, n):
                max_overlap = max(max_overlap, count_overlap(x_shift, y_shift))

        return max_overlap