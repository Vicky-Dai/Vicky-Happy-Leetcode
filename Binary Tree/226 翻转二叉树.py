#递归 前序遍历
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root #这个实际上的作用是作为最后返回根节点，如果不是因为这个其实没有必要写他  因为过程中你又不需要赋值 翻转是递归直接做到的
    
#要注意单边的二叉树，比如[2,3,null,1]


#后续遍历
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        self.invertTree(root.left)#从这里进入递归，直到叶子节点self.invertTree(root.left)返回None,接着往下执行,右侧也返回None,交换左右None，返回当前root（叶子节点），作为上一个递归函数的返回值
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root