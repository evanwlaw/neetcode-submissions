class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Idea: bfs from rotten rotten fruit. each 'layer' is a second of time. 
        if there is still fresh fruit, return -1

        1. find # of fresh and locate rotten to put into queue
        2. bfs through queue of rotten
            increment up to len(queue)
                go through 4 directions from the curr rotten fruit
                    if current position is valid and the fruit is fresh
                        turn fresh fruit to rotten and add to queue
        return result if fresh == 0 else -1

        """

        q = deque()
        time, fresh = 0,0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r,c])

        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        while q and fresh > 0:

            for i in range(len(q)):
                r, c = q.popleft()
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < rows and 0 <= col < cols and grid[row][col] == 1:
                        fresh -= 1
                        grid[row][col] = 2
                        q.append([row,col])
            time += 1

        return time if fresh == 0 else -1

