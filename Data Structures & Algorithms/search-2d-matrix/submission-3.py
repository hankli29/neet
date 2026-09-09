class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # sorted in non-decreasing order
        # first num of row is always > last num of prev row

        # binary search prolly

        l_row = 0
        r_row = len(matrix) - 1

        while l_row <= r_row:
            mid_row = int((l_row + r_row) / 2)
            tgt_row = matrix[mid_row]

            first = tgt_row[0]
            last = tgt_row[len(tgt_row) - 1]

            if target < first:
                r_row = mid_row - 1
            elif target > last:
                l_row = mid_row + 1
            else:
                # do regular bsearch

                l = 0
                r = len(tgt_row) - 1

                while l <= r:
                    mid = int((l + r) / 2)
                    cur = tgt_row[mid]

                    if cur > target:
                        r = mid - 1
                    elif cur < target:
                        l = mid + 1
                    else:
                        # target element found
                        return True
                
                return False

        return False


                