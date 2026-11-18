class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        
        """
        ROWS, COLS  = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        
        def dfs(r, c, visitSet, prevHeight):
            if ((r,c) in visitSet or
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                prevHeight > heights[r][c]):
                return
            visitSet.add((r,c))

            dfs(r-1,c,visitSet, heights[r][c])
            dfs(r+1,c,visitSet, heights[r][c])
            dfs(r,c-1,visitSet, heights[r][c])
            dfs(r,c+1,visitSet, heights[r][c])
            return

        for c in range(COLS):
            dfs(0, c, pacific, heights[0][c])
            dfs(ROWS-1, c, atlantic, heights[ROWS-1][c])
        
        for r in range(ROWS):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, COLS-1, atlantic, heights[r][COLS-1])
        
        output = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pacific and (r,c) in atlantic:
                    output.append([r,c])
        return output