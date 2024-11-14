import collections
from TreeNode import TreeNode

class Solution:
    def maxDepth(self, root: 'TreeNode') -> int:
        if not root:
            return 0
        queue = collections.deque([root])
        l = 0

        while queue:
            l += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
         
        return l


        
