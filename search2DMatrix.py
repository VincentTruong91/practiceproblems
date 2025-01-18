#double binary search
#time complexity -> O(log(m*n))
#space -> O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        top = 0
        bottom = len(matrix) - 1

        while (top <= bottom):
            middle = (top + bottom) // 2
            if matrix[middle][-1] < target:
                top = middle + 1
            elif matrix[middle][0] > target:
                bottom = middle - 1
            else: #we found the target in this row
                break

        #if none of the rows contains target value
        if not (top <= bottom):
            return False
        row = (top + bottom) // 2
        l = 0
        r = cols - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[row][m] < target:
                l = m + 1
            elif matrix[row][m] > target:
                r = m - 1
            else:
                return True

        return False

