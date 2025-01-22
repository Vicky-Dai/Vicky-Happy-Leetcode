#最小深度是从根节点到最近叶子节点的最短路径上的节点数量。注意是叶子节点。

#什么是叶子节点，左右孩子都为空的节点才是叶子节点！

class Solution:
    def getDepth(self, node):
        if node is None:
            return 0
        leftDepth = self.getDepth(node.left)  # 左
        rightDepth = self.getDepth(node.right)  # 右
        
        # 当一个左子树为空，右不为空，这时并不是最低点
        if node.left is None and node.right is not None:
            return 1 + rightDepth
        
        # 当一个右子树为空，左不为空，这时并不是最低点
        if node.left is not None and node.right is None:
            return 1 + leftDepth
        
        result = 1 + min(leftDepth, rightDepth)
        return result
# 这道题4.中间及最后返回值就很明显，要分三种情况，但是也没有脱离二叉树递归的结构
    def minDepth(self, root):
        return self.getDepth(root)
        #leftDepth 和 rightDepth 是通过递归调用计算得到的，必须在递归调用后才能准确得出左右子树的深度。
#如果提前判断是否有子树为空，会导致在计算深度时，递归尚未完成，数据不完整。