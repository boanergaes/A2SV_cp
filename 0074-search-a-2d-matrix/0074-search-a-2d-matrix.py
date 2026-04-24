class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_low, row_high, = 0, len(matrix) - 1
        ridx = -1

        while row_low <= row_high:
            mid = row_low + (row_high - row_low) // 2

            if target < matrix[mid][0]:
                row_high = mid - 1
            elif target > matrix[mid][-1]:
                row_low = mid + 1
            else:
                ridx = mid
                break
        else:
            return False
        
        row = matrix[ridx]

        low = 0
        high = len(row) - 1

        while low <= high:
            mid = (low + high) // 2

            if target > row[mid]:
                low = mid + 1
            elif target < row[mid]:
                high = mid - 1
            else:
                return True
        
        return False