class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        colums = len(grid[0])
        result = 0
        max_result = 0
        

        def dfs(c, r):

            if r < 0 or r >= rows or c < 0 or c >= colums:
                return 0

            if grid[r][c] == 0:
                return 0

            grid[r][c] = 0
            result =  1

            result += dfs(c + 1, r)
            result += dfs(c - 1, r)
            result += dfs(c, r + 1)
            result += dfs(c, r - 1)

            return result

        for r in range(rows):
            for c in range(colums):
                if grid[r][c] == 1:
                    area = dfs(c, r)
                    max_result = max(max_result, area)

        return max_result