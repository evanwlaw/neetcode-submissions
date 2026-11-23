class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        two sets
        dfs from top and bottom -> if prevHeight > heights[r][c], keep going
        dfs from left and right
        compare both sets
        """
        pacific, atlantic = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r,c, oceanSet, prevHeight):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                (r,c) in oceanSet or
                prevHeight > heights[r][c]):
                return
            oceanSet.add((r,c))

            dfs(r-1,c, oceanSet, heights[r][c])
            dfs(r+1,c, oceanSet, heights[r][c])
            dfs(r,c-1, oceanSet, heights[r][c])
            dfs(r,c+1, oceanSet, heights[r][c])
            return

        # dfs from top and bottom
        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])

        # dfs from left and right
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        
        output = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    output.append([r,c])
        return output