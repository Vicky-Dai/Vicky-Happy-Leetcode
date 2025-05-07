#在解决组合问题时，尤其是涉及到重复元素的组合（例如 candidates = [1, 1, 2]），我们需要确保：
#conception树层去重，树枝去重（不需要）同一层的递归中：不产生重复的组合。不同层之间：允许使用相同的元素。 
#树层去重要排序

class Solution:
    def backtracking(self, candidates, target, total, startIndex, path, result):
        if total == target:
            result.append(path[:])
            return

        for i in range(startIndex, len(candidates)):
            if i > startIndex and candidates[i] == candidates[i - 1]:  #去除重复组合 #也就是说，当 i 为 0 时，这个条件为 False，不会执行后面的判断，因此不会导致 i - 1 超出范围。
                continue #注意一定是i>startIndex,这样保证树层去重，树枝不去重  因为树枝每次递归进来都是从都开始，startIndex都是要用的

            if total + candidates[i] > target:
                break

            total += candidates[i]
            path.append(candidates[i])
            self.backtracking(candidates, target, total, i + 1, path, result)
            total -= candidates[i]
            path.pop()

    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        self.backtracking(candidates, target, 0, 0, [], result)
        return result