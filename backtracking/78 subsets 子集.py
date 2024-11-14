#如果把 子集问题、组合问题、分割问题都抽象为一棵树的话，那么组合问题和分割问题都是收集树的叶子节点，而子集问题是找树的所有节点！
class Solution:
    def subsets(self, nums):
        result = []
        path = []
        self.backtracking(nums, result, path, 0)
        return result
    
    def backtracking(self, nums, result, path, startIndex):
        result.append(path[:])
        # if startIndex < len(nums):  这句可以不写，下面i已经控制了
        for i in range(startIndex, len(nums)):
            path.append(nums[i])
            self.backtracking(nums, result, path, i+1)
            path.pop()
        
