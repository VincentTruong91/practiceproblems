#Hashset strategy
#Time complexity -> O(n^2) nested for loops
#Space complexity -> O(n^2) in memory bc it store sets for each row, column, and square. Total of 27 sets (9 column sets, 9 row sets, and 9 square sets) n=9, total of 81 tiles
from typing import List
from collections import defaultdict #provides default value for nonexistent key, avoids KeyError
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #sets because we only need to figure out if there are any duplicates
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) #key = (row/3,column/3)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if(board[r][c] in rows[r]
                or board[r][c] in cols[c]
                or board[r][c] in squares[r//3, column//3]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[r//3,c//3].add(board[r][c])
        
        return True