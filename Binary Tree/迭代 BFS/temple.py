#迭代BFS模板，也就是102题的解法

import TreeNode
import collections

class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        if not root:
            return []
        queue = collections.deque([root])
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                level.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(level)
        return result