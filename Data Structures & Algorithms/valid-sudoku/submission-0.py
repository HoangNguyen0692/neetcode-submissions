from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set)
        columns = defaultdict(set)
        squares = defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue

                # Identify the specific 3x3 square this cell belongs to
                square_coord = (r // 3, c // 3)

                if val in rows[r] or val in columns[c] or val in squares[square_coord]:
                    return False
                
                rows[r].add(val)
                columns[c].add(val)
                squares[square_coord].add(val)
            
        return True
                


        