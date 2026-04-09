class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        answer = set()

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == ".":
                    continue
                if ("row", i, val) in answer or  ("col", j, val) in answer or ("box", i//3, j//3, val) in answer:
                    return False
                answer.add(("row", i, val)) 
                answer.add(("col", j, val))
                answer.add(("box", i//3, j//3, val)) 
        return True 


# Input: board =
# [["1","2",".",".","3",".",".",".","."],
#  ["4",".",".","5",".",".",".",".","."],
#  [".","9","8",".",".",".",".",".","3"],
#  ["5",".",".",".","6",".",".",".","4"],
#  [".",".",".","8",".","3",".",".","5"],
#  ["7",".",".",".","2",".",".",".","6"],
#  [".",".",".",".",".",".","2",".","."],
#  [".",".",".","4","1","9",".",".","8"],
#  [".",".",".",".","8",".",".","7","9"]]

# Output: true