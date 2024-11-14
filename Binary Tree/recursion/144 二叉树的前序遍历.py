# 前序遍历-递归-LC144_二叉树的前序遍历
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        res = []

        def dfs(node):#内部函数不需要self
            if node is None:
                return
            
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)  #这里递归没有返回值，函数走到最后一行结束的时候，才会返回

        dfs(root) #调用函数  python先定义后调用 与js不同
        return res
    
    #dfs没有返回值：该函数的主要目的是进行深度优先搜索并收集节点的值。在这种情况下，结果存储在一个外部的列表（如 res）中，而不是通过返回值来传递。