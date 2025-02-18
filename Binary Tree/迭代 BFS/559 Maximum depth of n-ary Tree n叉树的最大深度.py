import Optional # type: ignore

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root:'Node') -> int:
        if not root:
            return 0
        
        max_depth = 1

        for child in root.children:
            max_depth = max(max_depth, self.maxDepth(child) + 1)
#对于每个节点，你会递归地调用 maxDepth 方法来计算该节点的所有子节点的最大深度。这个过程会一直递归下去，直到到达树的最深层（即叶子节点）。
        return max_depth

