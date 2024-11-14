#这个排列和46的区别就是，数组里面会有重复元素，所以要按照以前树层去重的思想sort一下然后used数组

class Solution:
    def permuteUnique(self, nums):
        nums.sort() #排序
        result = []
        path = []
        used = [False] * len(nums)
        self.backtracking(nums, result, path, used)
        return result  #不要忘记写

    def backtracking(self, nums, result, path, used):
        if len(path) == len(nums):
            result.append(path[:])
            return #记得要return

        for i in range(len(nums)):
            if (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]) or used[i]: #注意树层not used[i - 1] 回溯回来前一个还是False #让树枝如何知道取下一个： or used[i]
                continue
            used[i] = True
            path.append(nums[i])
            self.backtracking(nums, result, path, used)
            used[i] = False
            path.pop()
