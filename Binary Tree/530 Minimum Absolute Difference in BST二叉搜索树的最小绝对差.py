#利用中序递增，找到该树最小值

class Solution:
    def __init__(self):
        self.result = float('inf')  # 最小差值初始化为无穷大

    def traversal(self, cur, pre):
        if cur is None:
            return pre  # 返回当前子树最后访问的节点

        # 左子树递归
        pre = self.traversal(cur.left, pre)

        # 当前节点逻辑处理
        if pre is not None:  # 如果有上一个节点
            self.result = min(self.result, cur.val - pre.val)
        pre = cur  # 更新 pre 为当前节点

        # 右子树递归
        return self.traversal(cur.right, pre)

    def getMinimumDifference(self, root):
        self.traversal(root, None)
        return self.result

#转换成数组
class Solution:
    def __init__(self):
        self.vec = []

    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left)
        self.vec.append(root.val)  # 将二叉搜索树转换为有序数组
        self.traversal(root.right)

    def getMinimumDifference(self, root):
        self.vec = []
        self.traversal(root)
        if len(self.vec) < 2:
            return 0
        result = float('inf')
        for i in range(1, len(self.vec)):
            # 统计有序数组的最小差值
            result = min(result, self.vec[i] - self.vec[i - 1])
        return result
