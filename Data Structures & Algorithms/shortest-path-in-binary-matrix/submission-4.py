from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        bfs -> return shortest path len
        """
        if grid[0][0] != 0 or grid[-1][-1] != 0:
            return -1
        
        directions = [
            [-1,0], [1,0], [0,-1], [0,1],
            [-1,-1], [1,-1], [-1,1],[1,1]
        ]
        n = len(grid)

        queue = deque([[0,0,1]]) # r,c,cost
        grid[0][0] = 1

        while queue:
            r, c, cost = queue.popleft()
            if r == n - 1 and c == n - 1:
                return cost
            

            for dr, dc in directions:
                checkR, checkC = r + dr, c + dc
                if (checkR < 0 or checkR >= n or
                    checkC < 0 or checkC >= n or 
                    grid[checkR][checkC] != 0): # ignore invalid
                    continue
                queue.append([checkR, checkC, cost + 1])
                grid[r][c] = 1 # mark visited

        return -1