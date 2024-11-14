# 迭代法 前序
#遍历和处理节点的逻辑是分开的
from TreeNode import TreeNode

class Solution:
    def preorderTraversal(self, root:TreeNode) -> list[int]:
        if not root:
            return []
        res = []
        stack = [root]

        while stack:
            node = stack.pop() #取到栈顶的元素
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return res[::-1]
