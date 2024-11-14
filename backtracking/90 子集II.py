#78子集 和 40组合总和II去重的结合版
#求子集不需要写终止条件，因为直接被for循环限制住了，因为它是先写result.append  之前组合切割要终止条件才能找到需要的叶子节点
#这也是为什么组合切割的结果在叶子节点，而子集是所有的都收集
class Solution:
    def subsetsWithDup(self, nums):
        result = []  #可变对象作为参数传递的是指针
        path = []
        self.backtracking(nums, result, path, 0)
        return result
    def backtracking(self, nums, result, path, startIndex):
        result.append(path[:])
        for i in range(startIndex, len(nums)):
            if i > startIndex and nums[i] == nums[i-1]:
                continue
            path.append(nums[i])
            self.backtracking(nums, i+1, path, result)
            path.pop()
            
    