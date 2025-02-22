class Solution:
    def searchInMatrix(self, matrix: List[List[int]], target:int) -> bool:
        top, bottom = 0, len(matrix) - 1

        targetRow = []

        while top <= bottom:
            middle = (top + bottom) // 2

            middleLowest = matrix[middle][0]
            middleHighest = matrix[middle][-1]

            if target > middleHighest:
                top = middle + 1
            elif target < middleHighest:
                bottom = middle - 1
            else:
                targetRow = matrix[middle]
                break

        if not top <= bottom:
            return False

        l,r = 0, len(targetRow) - 1

        while l <= r:
            m = (l + r) // 2

            if target > m:
                l = m + 1
            elif target < m:
                r = m - 1
            else:
                return True 
            
        return False