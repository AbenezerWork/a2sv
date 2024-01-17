class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = []
        p = [0]*(len(matrix[0])+1)
        self.prefix.append(p)
        

        for i in range(len(matrix)):
            tmp = [0]
            for j in range(len(matrix[0])):
                curr = matrix[i][j] + self.prefix[i][j+1] + tmp[j] - self.prefix[i][j]
                tmp.append(curr)
            self.prefix.append(tmp)
            


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefix[row2+1][col2+1]+self.prefix[row1][col1]-self.prefix[row1][col2+1]-self.prefix[row2+1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)