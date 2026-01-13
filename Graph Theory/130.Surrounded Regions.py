# The same as 沉没孤岛，只是需要额外处理边界 沉没孤岛可以把边界上的0全都改成海洋，这样剩下的1就是被包围的陆地
# 1. Mark boundary connected O's
# 2. Convert surrounded O → X
# 3. Restore # → O

class Solution:
    def solve(self, board):
        if not board:
            return
        
        m, n = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != 'O':
                return
            board[x][y] = '#'
            dfs(x+1, y)
            dfs(x-1, y)
            dfs(x, y+1)
            dfs(x, y-1)

        # 1. Mark boundary connected O's
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        # 2. Convert surrounded O → X
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        # 3. Restore # → O
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
