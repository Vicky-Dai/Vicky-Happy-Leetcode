class Solution:
    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total == target:
            result.append(path[:])
            return
        for i in range(startIndex, len(candidates)):
            if total + candidates[i] > target:
                break #剪枝操作
            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i, path, result) #不用i+1因为可以重复使用 重复的数字相加，如果打了就退回去一个
            total -= candidates[i]
            path.pop()

    def combinationSum(self, candidates, target):
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, [], result)
        return result