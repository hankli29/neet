class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_l = 0
        row_r = len(matrix) - 1

        # first int of every row > last int of prev row
        # index into row, if target < first element, can discard that row
            # and all following rows
        # if target > first element, then if target > last element of row,
            # can discard current and all previous rows
        
        while row_l < row_r:
            row_idx = int((row_l + row_r) / 2)
            row_mid = matrix[row_idx]

            if target < row_mid[0]:
                row_r = row_idx - 1

            elif target > row_mid[0]:
                if target > row_mid[-1]:
                    row_l = row_idx + 1
                else: # within the same row
                    row_l = row_r = row_idx
            else:
                return True
        
        # after narrowing down to single row, do normal bsearch
        row = matrix[row_l]
        l = 0
        r = len(row) - 1

        while l <= r:
            idx = int((l + r) / 2)
            mid = row[idx]

            if target > mid:
                l = idx + 1
            elif target < mid:
                r = idx - 1
            else:
                return True
                
        return False

        