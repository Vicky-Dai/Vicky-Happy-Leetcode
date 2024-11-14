#递归法 后序 其实求的是高度
from TreeNode import TreeNode

class Solution:
    def maxdepth(self, root: TreeNode) -> int:
            return self.getdepth(root)
        
    def getdepth(self, node):
        if not node:
            return 0
        leftheight = self.getdepth(node.left) #左
        rightheight = self.getdepth(node.right) #右
        height = 1 + max(leftheight, rightheight) #中
        return height
    #中处理用了回溯，在递归返回的过程进行处理，因此它的水平面是最底层，也就是求得是高度
    
#精简版
class Solution:
    def maxdepth(self, root: TreeNode)-> int:
        if not root:
            return 0
        return 1 + max(self.maxdepth(root.left), self.maxdepth(root.right))


#深度
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.getDepth(root, 0)  # 从根节点开始，初始深度为 0

    def getDepth(self, node: TreeNode, depth: int) -> int:
        if not node:
            return depth  # 如果节点为空，返回当前深度
        # 递归计算左子树和右子树的深度，深度加 1
        leftDepth = self.getDepth(node.left, depth + 1) #把根节点的1算进去了
        rightDepth = self.getDepth(node.right, depth + 1)
        return max(leftDepth, rightDepth)  # 中 返回较大深度        
    #直接在递归的进程中进行计算（depth + 1） 从上到下，求得是深度