# 后序遍历-递归-LC145_二叉树的后序遍历
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.value = val
        self.right = right
        self.left = left

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        
        def dfs(node):
            if node is None:
                return
            
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)

        dfs(root)
        return res