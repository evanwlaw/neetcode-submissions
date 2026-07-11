class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        
        Iterate through board. 
            If current cell is the first letter of word:
                DFS - go through directions around cell to look for next letter
                    - if DFS is True, then we found word
        Time complexity: O(m * 4^n) - m is the num of cells in entire board. n is the len of word. For each cell, we can possibly go through all 4 directions for the n len of word - O(m * 4^n)
        Space Complexity: O(n) - DFS recursion stack uses most space. We would make at most n DFS calls where n is the len of the given word.
        '''
        ROWS, COLS = len(board), len(board[0])

        def dfs(r: int, c: int, i: int):
            if i == len(word):
                return True
            # check if valid
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[i]
            ):
                return False
            
            # dfs search around cell.
            temp = board[r][c] 
            board[r][c] = "#" # mark as in-use for current path.
            search = ( 
                dfs(r - 1,c, i + 1) or
                dfs(r + 1,c, i + 1) or
                dfs(r, c - 1, i + 1) or
                dfs(r, c + 1, i + 1) 
            )

            board[r][c] = temp # remove placeholder as path is not in-use
            return search
                

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        return False