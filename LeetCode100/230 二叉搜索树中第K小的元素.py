class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = 0  # 用于记录访问的节点数
        self.result = None  # 用于存储第k小的元素
        
        def dfs(node):
            if node is None or self.count >= k:  # 如果节点为空，或已经找到了第k小元素
                return
            # 先遍历左子树
            dfs(node.left)
            # 访问当前节点
            self.count += 1
            if self.count == k:
                self.result = node.val  # 找到第k小的元素，存入self.result
                return  # 找到后可以直接停止递归
            # 继续遍历右子树
            dfs(node.right)
        # 执行深度优先搜索（中序遍历）
        dfs(root)
        return self.result  # 返回找到的第k小元素
