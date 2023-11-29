class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        for i in range(len(matrix)):
            j = 0
            check = matrix[i][j]
            while i<len(matrix) and j<len(matrix[0]):
                if check != matrix[i][j]:
                    return False
                i+=1
                j+=1
        
        for j in range(len(matrix[0])):
            i = 0
            check = matrix[i][j]
            while i<len(matrix) and j<len(matrix[0]):
                if check != matrix[i][j]:
                    return False
                i+=1
                j+=1
        return True

        