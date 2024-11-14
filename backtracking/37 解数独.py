#和51 N皇后相比，这道题是一个二维递归（一个backtracking，两层for），因为这个行列每个点都要填满数字  这里有三个for是因为，这道题把以前交给递归的参数的一份工作单独拿出来给for干了（第三个for）
#backtracking的返回值为bool，因为就一个结果，找到了直接一路返回True，其他都不搜了
#但是以前组合分割子集，都是有多个结果，返回值为void，直接把结果在路上都捡到result里面
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtracking(board) #最上层递归

    def backtracking(self, board: List[List[str]]) -> bool:
        # 若有解，返回True；若无解，返回False
        for i in range(len(board)): # 遍历行
            for j in range(len(board[0])):  # 遍历列
                # 若空格内已有数字，跳过
                if board[i][j] != '.': continue
                for k in range(1, 10):
                    if self.is_valid(i, j, k, board):
                        board[i][j] = str(k)
                        if self.backtracking(board): return True #管理除了最上层递归的所有递归
                        board[i][j] = '.'
                # 若数字1-9都不能成功填入空格，返回False无解
                return False
        return True # 有解 给最上层递归返回值
    
    def is_valid(self, row: int, col: int, val: int, board: List[List[str]]) -> bool:
        # 判断同一行是否冲突
        for i in range(9):
            if board[row][i] == str(val):
                return False
        # 判断同一列是否冲突
        for j in range(9):
            if board[j][col] == str(val):
                return False
        # 判断同一九宫格是否有冲突
        #找到所在小九宫格的起始点位
        start_row = (row // 3) * 3 #row // 3：将当前的行号 row 整除 3，得到该数字所在的 3x3 小宫格是从上到下的第几个小宫格。
        start_col = (col // 3) * 3 #乘以 3：通过 (row // 3) * 3 和 (col // 3) * 3，我们计算出该数字所在的小宫格的左上角（即该小宫格的第一行第一列）的坐标。
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == str(val):
                    return False
        return True