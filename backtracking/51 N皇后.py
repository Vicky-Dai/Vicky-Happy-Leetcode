#其实逻辑跟之前的寻找某种符合的组合的道理是一样的，仍然是一维递归（一个for一个backtracking）只不过换成了二维数组找结果，要注意一下xy表示即可
#递归用来遍历行，for用来遍历列
class Solution:
    def soveNQueens(self, n:int) -> list[list[str]]:
        result = [] #最后把不同的二维数组棋盘结果放进去，最后变成一个三维数组
        chessboard = ['.'*n for _ in range(n)] #初始化一个二维数组棋盘
        self.backtracking(n, 0, chessboard, result)
        return result
    
    def backtracking(self, n, row, chessboard, result) -> None:
        if row == n: #row虽然是从0开始的，但是必须把最后一层走完，然后再递的时候就到这了，并没有把超出的一层再走完
            result.append(chessboard[:])
            return 
        
        for col in range(n):
            if self.isValid(row, col, chessboard):
                chessboard[row] = chessboard[row][:col] + 'Q' + chessboard[row][col+1:]   #'str' object does not support item assignment
                self.backtracking(n, row+1, chessboard, result)
                chessboard[row] = chessboard[row][:col] + '.' + chessboard[row][col+1:]  #回溯 恢复到上次递归的转改（栈里的临时变量）

        def isValid(self, row, col, chessboard) -> bool:
            #检查列:同一列不能有
            for i in range(row):
                if chessboard[i][col] == 'Q':
                    return False
            #检查对角线：注意因为放置的时候是按照行的顺序放的，也就是说当前放的Q只有上面的行有已经放过的Q，所以只搜左上和右上    
            #45度 左上
            i, j = row - 1, col - 1 #更新一下
            while i >= 0 and j >= 0:
                if chessboard[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            #135度 右上
            i, j = row - 1, col -1
            while i >= 0 and j < len(chessboard):
                if chessboard[i][j] == 'Q':
                    return False 
                i -= 1
                j += 1

            return True



