class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        left = 0
        right = len(matrix[0])
        top = 0
        down = len(matrix)

        result = []

        while left < right and top < down:

            for i in range(left, right):
                result.append(matrix[top][i])

            top += 1

            for i in range(top, down):
                result.append(matrix[i][right - 1])

            right -= 1

            if not (left < right and top < down):
                break

            for i in range(right - 1, left - 1, -1):
                result.append(matrix[down - 1][i])

            down -= 1

            for i in range(down - 1, top - 1, -1):
                result.append(matrix[i][left])
            
            left += 1

        return result
