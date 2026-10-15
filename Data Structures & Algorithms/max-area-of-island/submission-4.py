class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0], [1,0], [0,-1], [0,1]]
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c):
            if (0 > r or r >= ROWS or
                0 > c or c >= COLS or
                grid[r][c] != 1):
                return 0
            
            grid[r][c] = 0
            area = 1 # current cell area contribution

            for dr, dc in directions:
                area += dfs(dr + r, dc + c)
            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r,c))
        return maxArea
