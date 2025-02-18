class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
#在 Python 中，当你定义函数（包括构造函数 __init__）时，如果你为某些参数指定了默认值，所有在其后的参数必须也有默认值。

class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []

        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res