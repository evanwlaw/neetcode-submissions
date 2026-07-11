from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Iterate through grid. 
            If fresh fruit, increment counter (there might be case where fresh fruit is not touching rotten)
            If we find a rotten fruit add to queue for BFS.
            
        
        BFS while we still have rotten fruit in queue and while fresh fruit on grid
            For each 4-dir of rotten fruit:
                if fresh turn rotten
            Each layer of BFS is +1 to time.
        
        Time Complexity: O(m*n) - Where m is the num of grid rows and n is the grid cols. We iterate through entire grid in first for loop. Worst case in BFS is that we have to iterate through entire grid.
        Space Complexity: O(m*n) - Extra space is used for the queue. Worst case is if all cells on grid are rotten and we have to enqueue everything.
        '''
        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        time, freshFruit = 0, 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        # Find all rotten and enqueue
        # Find num of fresh fruit
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    freshFruit += 1
                if grid[r][c] == 2:
                    queue.append([r,c])

        # bfs while loop
        while queue and freshFruit > 0:
            for i in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    check_r, check_c = r + dr, c + dc

                    # check and process if valid
                    if (check_r >= 0 and check_r < ROWS and
                        check_c >= 0 and check_c < COLS and
                        grid[check_r][check_c] == 1
                    ):  
                        grid[check_r][check_c] = 2
                        freshFruit -= 1
                        queue.append([check_r, check_c])
            time += 1
        return time if freshFruit == 0 else -1
