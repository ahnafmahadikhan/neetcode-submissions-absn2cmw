class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols, rows = len(matrix[0]), len(matrix)

        left, right = 0, cols * rows - 1
        
        while left <= right:
            mid = (left + right) // 2
            r = mid // cols
            c = mid % cols
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return False
            