class Solution:
    def combinationSum3(self, k: int, n:int) -> list[list[int]]:
        result = [] #存放结果集
        self.backtracking(n, k, 0, 1, [], result)

    def backtracking(Self, targetSum, k, currentSum, startIndex, path, result):
        if currentSum > targetSum: #剪枝操作
            return
        if len(path) == k:
            if currentSum == targetSum:
                result.append(path[:])
            return
        for i in range(startIndex, 9 - (k - len(path)) + 2):
            currentSum += i #处理
            path.append(i) #处理
            self.backtracking(targetSum, k, currentSum, i+1, path, result) #注意i+1调整index
            currentSum -= i
            path.pop()