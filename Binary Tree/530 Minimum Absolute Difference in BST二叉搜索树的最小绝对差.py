#利用中序递增，找到该树最小值
class Solution:
    def __init__(self):
        self.result = float('inf')

    def traversal(self, cur):
        if cur is None:
            return
        self.traversal(cur.left)
        if self.pre is not None:
            self.result = min(self.result, cur.val - self.pre.val)
        self.pre = cur
        self.traversal(cur.right)

    def getMinimumDifference(self, root) -> int:
        self.traversal(root)
        return self.result
        