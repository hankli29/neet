class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # check rows
        for row in board:
            rseen = set()
            for cell in row:
                if cell.isdigit():
                    if cell not in rseen:
                        rseen.add(cell)
                    else:
                        return False
        
        # check columns
        for c in range(len(board)):
            cseen = set()
            for r in range(len(board)):
                cell = board[r][c]
                if cell.isdigit():
                    if cell not in cseen:
                        cseen.add(cell)
                    else:
                        return False
        
        # check boxes
        for row in range(3):
            for col in range(3):

                seen = set()

                for r_idx in range(row * 3, row * 3 + 3):
                    for c_idx in range(col * 3, col * 3 + 3):
                        cell = board[r_idx][c_idx]

                        if cell.isdigit():
                            if cell not in seen:
                                seen.add(cell)
                            else:
                                return False

        return True

                # when row = 0, col = 0, in the first box
                # how to iterate through [0, 2] for both r_idx and c_idx
                
                # row=1, col=2, in sixth box
                # how to iterate through [3, 5] for r_idx and [6, 8] for c_idx
        

        
        
