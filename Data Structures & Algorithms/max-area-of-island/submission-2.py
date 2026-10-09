class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        keep a maxArea variable to track

        iterate through grid
            if cell == 1, then dfs
                dfs and mark seen cells as 0 so we don't go over it again.
                    in dfs, only dfs into valid cells
                        valid cell = within grid limits and == 1
                        increment island area as long as we see a valid cell
        return maxArea

        Time: O(m*n) - where m is num of rows and n is num cols. we skip all seen islands so we would traverse through each cell at most once
        Space: O(m*n) - recursive call stack. worst case the entire grid is an island and we need to traverse through entire thing
        """

        # ROWS, COLS = len(grid), len(grid[0])
        # directions = [[-1,0],[1,0], [0,-1],[0,1]]
        # maxArea = 0

        # def dfs(r, c, islandArea):
            
            
        #     islandArea += 1
        #     grid[r][c] = 0

        #     for dr, dc in directions:
        #         checkR, checkC = dr + r, dc + c
        #         if (0 <= checkR < ROWS and
        #             0 <= checkC < COLS and
        #             grid[checkR][checkC] == 1):
        #             islandArea += dfs(checkR, checkC, islandArea)
        #     return islandArea

        # for row in range(ROWS):
        #     for col in range(COLS):
        #         if grid[row][col] == 1:
        #             maxArea = max(maxArea, dfs(row,col, 0))
        
        # return maxArea

        """
        right track but we can acutall add up the areas around cell via dfs
        """

        ROWS, COLS = len(grid), len(grid[0])
        maxArea = 0

        def dfs(r, c, islandArea):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == 0):
                return 0

            grid[r][c] = 0

            islandArea = (
                dfs(r+1, c, islandArea) +
                dfs(r-1, c, islandArea) +
                dfs(r, c+1, islandArea) +
                dfs(r, c-1, islandArea)
            )

            return islandArea + 1

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, dfs(row,col, 0))
        
        return maxArea
