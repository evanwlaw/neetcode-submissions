class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        input is a grid board
        - row  is 1-9 without dupes
        - col is 1-9 without dupes
        - each 3x3 box is 1-9 without dupes
        - does not need to be solvable -> figure out if current state of grid has valid row, col and subboxes

        Need to iterate through entire grid to figure out if grid is valid.

        ex1:
        at [0][0], we see value of 1. at this point: row, col, subsquares is valid. what we don't know if we move on is if the value of current cell remains valid or invalidates another cell later.
        

        at [0][1], we see value of 2. at this point: row, col, subsquares is valid. what we don't know if we move on is if the value of current cell remains valid or invalidates another cell later. we don't see the previous 1. what if previous was a 2? we wouldnt know,but current cell would invalidate the row and the subsquares

        we skip empty cells to go to [0][4], value of 3. at this point: row, col, subsquares is valid. what we don't know if we move on is if the value of current cell remains valid or invalidates another cell later. we don't see the previous 2. what if previous was a 3? we wouldnt know, but current cell would invalidate the row and the subsquares.
        
        we need several things:
        Sets for each rows
        Sets for each cols
        Sets for each the subsquares

        we can use hashmaps to hold the sets:
        rows -> row # : row's set()
        cols -> col # : col's set()
        sub_sq -> sub_sq # : sq square's set()

        each set holds the values seen so far. if we find a new cell's value exists in either of those sets, then return false
        

        """
        rows = defaultdict(set)
        cols = defaultdict(set)
        sub_sq = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                
                check = board[r][c]
                if (check in rows[r] or
                    check in cols[c] or
                    check in sub_sq[(r // 3, c // 3)]
                ):
                    return False
                rows[r].add(check)
                cols[c].add(check)
                sub_sq[(r // 3, c // 3)].add(check)
        return True
