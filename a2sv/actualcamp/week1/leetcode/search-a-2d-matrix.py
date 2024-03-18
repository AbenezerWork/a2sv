class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix)
        m = len(matrix[0])
        l,r = -1, n*m
        while r-l>1:
            mid = l+(r-l)//2
            x = mid//m
            y = mid%m
            if matrix[x][y]>target:
                r = mid
            else:
                l = mid
        if matrix[l//m][l%m]!= target:
            return False
        return True