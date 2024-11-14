#递归 前序 修改root1  节省时间空间
from TreeNode import TreeNode

class Solution:
    def mergeTrees(self, root1:TreeNode, root2:TreeNode) ->TreeNode:
        if not root1:
            return root2
        if not root2:
            return root1
        
        root1.val += root2.val #利用root1 在它上面进行加
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

        return root1