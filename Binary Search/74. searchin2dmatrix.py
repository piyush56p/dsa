class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1
        while(row<len(matrix) and col >= 0):
            if(matrix[row][col] == target):
                return True
            elif(matrix[row][col] > target):
                col = col -1
            else:
                row = row + 1
        else:
            return False
