from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        return shortest path -> bfs
        
        if [0][0] != 0 -> return False

        
        """
        if grid[0][0] != 0:
            return -1

        ROWS, COLS = len(grid), len(grid[0])
        # output = 1
        directions = [(-1, 0), (1,0), (0,-1), (0,1),
                        (-1,-1), (-1,1), (1,-1), (1,1)]

        queue = deque([(0,0)])
        visited = set((0,0))
        output = 1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                if r == ROWS-1 and c == COLS-1:
                    return output

                for dr, dc in directions:
                    checkR, checkC = dr + r, dc + c

                    if (checkR < 0 or checkR >= ROWS or
                        checkC < 0 or checkC >= COLS or
                        grid[checkR][checkC] != 0 or
                        (checkR, checkC) in visited):
                        continue
                    queue.append((checkR,checkC))
                    visited.add((checkR,checkC))
            output += 1
        return -1



