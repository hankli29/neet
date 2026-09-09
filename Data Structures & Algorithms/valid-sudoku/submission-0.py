class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # sub boxes
        start = 0
        subBoxes = [[] for i in range(9)]
        i = 0
        while i < len(board):
            for _ in range(3):
                for j in range(len(board[i])):
                    subBoxes[start + (j // 3)].append(board[i][j])
                i += 1
            start += 3
        for i in subBoxes:
            sub = []
            for j in i:
                if j != ".":
                    sub.append(j)
            if len(sub) != len(set(sub)):
                return False

        # row
        for i in board:
            row = []
            for j in i:
                if j != ".":
                    row.append(j)
            if len(row) != len(set(row)):
                return False
        
        # column
        columns = [[] for i in range(9)]
        for i in board:
            for j in range(len(i)):
                columns[j].append(i[j])
        for i in columns:
            column = []
            for j in i:
                if j != ".":
                    column.append(j)
            if (len(column) != len(set(column))):
                return False
        return True
