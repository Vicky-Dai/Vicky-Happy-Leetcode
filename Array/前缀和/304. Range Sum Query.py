# Attention: definition of preSum: preSum[i][j] = sum of matrix[0][0] to matrix[i-1][j-1]
# Draw a picture to understand the preSum and sumRegion function
from typing import List

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.preSum = [[0]*(m+1) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, m+1):
                self.preSum[i][j] = self.preSum[i-1][j] + self.preSum[i][j-1] + matrix[i-1][j-1] - self.preSum[i-1][j-1]
# To record the preSum, how to get sum of matrix[0][0] to matrix[i-1][j-1]?
# left part + upper part - overlap part + current element

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1] - self.preSum[row2+1][col1] - self.preSum[row1][col2+1] + self.preSum[row1][col1]

