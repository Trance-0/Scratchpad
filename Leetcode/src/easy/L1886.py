class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        # rotate mat for 90 degrees
        def rotate(mat):
            n=len(mat)
            for i in range(n):
                for j in range(i,n):
                    mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
            for i in range(n):
                for j in range(n//2):
                    mat[i][j],mat[i][n-1-j]=mat[i][n-1-j],mat[i][j]
            return mat
        
        for i in range(4):
            if mat==target:
                return True
            mat=rotate(mat)
        return False