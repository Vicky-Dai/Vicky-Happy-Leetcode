#这道题排列 和之前不同，不用startindex，因为每次都是从头开始，所以没法用startindex，只好用used数组来记录是否用过
class Solution:
    def permute(self, nums):
        result = []
        self.backtracking (nums, [], [False]*len(nums), result)
        return result 
          
    def backtracking(self, nums, path, used, result):
        if len(path) == len(nums):
            result.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, path, used, result)
            path.pop()
            used[i] = False