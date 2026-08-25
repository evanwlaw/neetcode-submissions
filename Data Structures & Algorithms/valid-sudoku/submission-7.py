from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, sub_sq = defaultdict(set), defaultdict(set), defaultdict(set)

        for r in range(9):
            for c in range(9):
                cell_val = board[r][c]
                # skip blanks
                if cell_val == ".":
                    continue

                # found a dupe, return false
                if (cell_val in rows[r] or
                    cell_val in cols[c] or
                    cell_val in sub_sq[(r//3, c//3)]
                ):
                    return False
                
                # otherwise, first time seen add to sets
                rows[r].add(cell_val)
                cols[c].add(cell_val)
                sub_sq[(r//3, c//3)].add(cell_val)
        return True