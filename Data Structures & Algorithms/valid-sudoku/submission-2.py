class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # verify all rows
        for row in board:
            counts = {}
            
            for col in row:
                counts[col] = counts.setdefault(col, 0) + 1

                if col != "." and counts[col] > 1:
                    return False
        
        # verify all cols
        c_idx = 0
        while c_idx < 9:
            counts = {}
            for row in board:

                cell = row[c_idx]
                counts[cell] = counts.setdefault(cell, 0) + 1

                if cell != "." and counts[cell] > 1:
                    return False
            c_idx += 1

        # verify each sub-grid
        # row/col vary from 0 to 2, index range in actual board can be found
        # using row/col * 3 to row/col * 3 + 3

        for row in range(3):
            for col in range(3):
                counts = {}
                for r in range(row * 3, row * 3 + 3):
                    for c in range(col * 3, col * 3 + 3):

                        cell = board[r][c]

                        counts[cell] = counts.setdefault(cell, 0) + 1

                        if cell != "." and counts[cell] > 1:
                            return False
                    
                        

        return True