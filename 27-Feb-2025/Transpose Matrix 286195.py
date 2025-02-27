# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:  
            return []

        rows, cols = len(matrix), len(matrix[0])
        transposed = [[0] * rows for _ in range(cols)]  # Initialize transposed matrix

        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]

        return transposed