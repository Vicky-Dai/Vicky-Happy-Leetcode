#平时我们解二叉树的题目时，已经习惯了通过节点的左右孩子判断本节点的属性，而本题我们要通过节点的父节点判断本节点的属性。

from TreeNode import TreeNode

class Solution:
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0  #终止条件
        
        leftValue = self.sumOfLeftLeaves(root.left) #左
        if root.left and not root.left.left and not root.left.right: #左子树是左叶子
            leftValue = root.left.val
        
        rightValue = self.sumOfLeftLeaves(root.right) #右

        sum_val = leftValue + rightValue #中
        return sum_val