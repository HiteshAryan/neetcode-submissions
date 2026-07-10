class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            hashset = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in hashset:
                    return False
                elif board[i][j] != ".":
                    hashset.add(board[i][j])
        
        for i in range(9):
            hashset = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] in hashset:
                    return False
                elif board[j][i] != ".":
                    hashset.add(board[j][i])
        
        for l in range(0,9,3):
            for k in range(0,9,3):
                hashset = set()
                for i in range(k,k+3):
                    for j in range(l,l+3):
                        if board[i][j] != "." and board[i][j] in hashset:
                            return False
                        elif board[i][j] != ".":
                            hashset.add(board[i][j])

        return True