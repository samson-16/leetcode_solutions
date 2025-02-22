class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        
        for i in range(1,cols):
            self.matrix[0][i] = self.matrix[0][i-1] + self.matrix[0][i]
        for i in range(1,rows):
            self.matrix[i][0] = self.matrix[i-1][0] + self.matrix[i][0]
        print(self.matrix)
        for r in range(1,rows):
            for c in range(1,cols):
                self.matrix[r][c] = self.matrix[r-1][c] + self.matrix[r][c-1] - self.matrix[r-1][c-1]+self.matrix[r][c]
        print(self.matrix)
        


    
     
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if not self.matrix:
            return 0


        total = self.matrix[row2][col2]
        top = self.matrix[row1-1][col2] if row1 > 0 else 0
        left = self.matrix[row2][col1-1] if col1 > 0 else 0
        top_left = self.matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0

        return total - top - left + top_left


   


        



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


   


        


