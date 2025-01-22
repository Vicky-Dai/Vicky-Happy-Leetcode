# 前序遍历-递归-LC144_二叉树的前序遍历
# Definition for a binary tree node.
""" 两个解法分别经典体现了递归的两种思路：遍历和分治 """

# 解法一：traverse遍历 无返回值
class Solution:
    def __init__(self):
        self.res = []
    
    # 返回前序遍历结果
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.traverse(root)
        return self.res

    # 二叉树遍历函数
    def traverse(self, root: TreeNode):
        if root is None:
            return
        # 前序位置
        self.res.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)

# 解法二：分解问题思路，单纯用题目给的preorder函数递归
#我们知道前序遍历的特点是，根节点的值排在首位，接着是左子树的前序遍历结果，最后是右子树的前序遍
#一棵二叉树的前序遍历结果 = 根节点 + 左子树的前序遍历结果 + 右子树的前序遍历结果。
class Solution:
    # 定义：输入一棵二叉树的根节点，返回这棵树的前序遍历结果
    def preorderTraversal(self, root):
        res = []
        if root == None:
            return res
        # 前序遍历的结果，root.val 在第一个
        res.append(root.val)
        # 利用函数定义，后面接着左子树的前序遍历结果
        res.extend(self.preorderTraversal(root.left))
        # 利用函数定义，最后接着右子树的前序遍历结果
        res.extend(self.preorderTraversal(root.right)) 
        return res
    
""" 综上，遇到一道二叉树的题目时的通用思考过程是：

1、是否可以通过遍历一遍二叉树得到答案？如果可以，用一个 traverse 函数配合外部变量来实现。

2、是否可以定义一个递归函数，通过子问题（子树）的答案推导出原问题的答案？如果可以，写出这个递归函数的定义，并充分利用这个函数的返回值。

3、无论使用哪一种思维模式，你都要明白二叉树的每一个节点需要做什么，需要在什么时候（前中后序）做。

本站 
二叉树递归专项练习 中列举了 100 多道二叉树习题，完全使用上述两种思维模式手把手带你练习，助你完全掌握递归思维，更容易理解高级的算法。 """