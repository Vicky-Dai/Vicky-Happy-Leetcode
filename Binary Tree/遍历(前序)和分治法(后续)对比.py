#力扣第 104 题「二叉树的最大深度为例

# 递归前序遍历（遍历法）
class Solution:
    def __init__(self):
        # 记录最大深度
        self.res = 0
        # 记录遍历到的节点的深度
        self.depth = 0

    def maxDepth(self, root: TreeNode) -> int:
        self.traverse(root)
        return self.res

    # 二叉树遍历框架
    def traverse(self, root: TreeNode) -> None:
        if root is None:
            return
        # 前序位置
        self.depth += 1
        if root.left is None and root.right is None:
            # 到达叶子节点，更新最大深度
            self.res = max(self.res, self.depth)
        self.traverse(root.left)
        self.traverse(root.right)
        # 后序位置
        self.depth -= 1

# 递归前序遍历（分治法）
class Solution:
    # 定义：输入根节点，返回这棵二叉树的最大深度
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        # 利用定义，计算左右子树的最大深度
        leftMax = self.maxDepth(root.left)
        rightMax = self.maxDepth(root.right)
        # 整棵树的最大深度等于左右子树的最大深度取最大值，
        # 然后再加上根节点自己
        res = max(leftMax, rightMax) + 1

        return res