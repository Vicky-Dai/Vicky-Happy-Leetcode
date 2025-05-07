class Solution:
    def tictactoe(self, moves: list[list[int]]) -> str:
        board = [[0]*3 for _ in range(3)]
        turn = 1  # A为1，B为-1
        
        for r, c in moves:
            board[r][c] = turn
            turn *= -1

        lines = []

        # 行和列
        for i in range(3):
            lines.append(sum(board[i]))          # 第i行
            lines.append(board[0][i] + board[1][i] + board[2][i])  # 第i列

        # 两条对角线
        lines.append(board[0][0] + board[1][1] + board[2][2])
        lines.append(board[0][2] + board[1][1] + board[2][0])

        for line in lines:
            if line == 3:
                return "A"
            elif line == -3:
                return "B"

        return "Draw" if len(moves) == 9 else "Pending"
