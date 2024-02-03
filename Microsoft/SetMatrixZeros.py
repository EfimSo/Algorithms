# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# Solution in O(mn) time and O(1) space
# Returns nothinng, modifies matrix in place

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        col0 = False

        # Use the  first cell of every row and column to track if row/col has been set to 0
        # Since we cannot use matrix[0][0] as an indicator for both row and column 0,
        # add a variable col0 where True == 0 (set to 0) and False == nonzero

        # Determine which rows and columns will be set to 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0:
                        matrix[0][0] = 0
                    if j == 0:
                        col0 = True
                    else:
                        matrix[i][0], matrix[0][j] = 0, 0
        
        # Check rows 1 to m for zeros
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        
        # Check columns 1 to n for zeros
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0
        
        # Check first row
        if matrix[0][0] == 0:
             for j in range(n):
                    matrix[0][j] = 0
        
        # Check first column
        if col0:
            for i in range(m):
                    matrix[i][0] = 0