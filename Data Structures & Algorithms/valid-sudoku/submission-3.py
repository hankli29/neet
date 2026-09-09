class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for r in board:
            seen = set()
            for c in r:
                if c != "." and c in seen:
                    return False
                
                seen.add(c)
        
        # check cols
        for col in range(9): # check each of 9 columns
            seen = set()
            for row in board:
                if row[col] != "." and row[col] in seen:
                    return False
                
                seen.add(row[col])
        
        # check 3x3 boxes in board
        # row idx = r * 3 to r * 3 + 3
        # col idx = c * 3 to c * 3 + 3
        for r in range(3):
            for c in range(3):
                seen = set()

                for r_idx in range(r * 3, r * 3 + 3):
                    for c_idx in range(c * 3, c * 3 + 3):
                        element = board[r_idx][c_idx]

                        if element != "." and element in seen:
                            return False
                        
                        seen.add(element)
        
        return True





            