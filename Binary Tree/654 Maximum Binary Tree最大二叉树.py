#构造二叉树一定要用前序 这样才能逐渐构建 
from TreeNode import TreeNode
class Solution:
    def constructMaximumBinaryTree(self, nums: list[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0]) #递归退出条件
        
        #中逻辑
        maxValue = 0
        maxValueIndex = 0
        for i in range(len(nums)):
            if maxValue < nums[i]:
                maxValue = nums[i]
                maxValueIndex = i
        root = TreeNode(maxValue, None)
        #maxValueIndex的必要性：你在循环中寻找了最大值，但没有保存它的索引。因此，当你在后面使用 i 切片数组以构建左子树和右子树时，i 始终是循环的最后一个索引，这不是你想要的。

        #左
        if maxValueIndex > 0: #如果是0，左侧已经没有节点，没有必要构造，所以不考虑相等
            new_list = nums[:maxValueIndex] #作用域在这个if code block里面，所以跟下面的不冲突 注意这个用法 ！
            root.left = self.constructMaximumBinaryTree(new_list) #实例化方法一定要用self.

        #右
        if maxValueIndex < len(nums) -1:
            new_list = nums[maxValueIndex+1:]
            root.right = self.constructMaximumBinaryTree(new_list)

        return root

        

