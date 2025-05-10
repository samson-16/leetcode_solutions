# Last updated: 5/10/2025, 7:15:09 PM
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n , m = len(matrix), len(matrix[0])
        for i in range(n-1,-1,-1):
            if matrix[i][0]<=target:
                if target in matrix[i]:
                    return  True
        return False

        