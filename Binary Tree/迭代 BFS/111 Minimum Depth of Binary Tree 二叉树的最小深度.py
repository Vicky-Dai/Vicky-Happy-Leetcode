import collections
from TreeNode import TreeNode
#需要注意的是，只有当左右孩子都为空的时候，才说明遍历的最低点了。如果其中一个孩子为空则不是最低点
class Solution:
    def minDepth(self, root:'TreeNode') ->int:
        if not root:
            return 0
        queue = collections.deque([root])
        minDepth = 0

        while queue:
            minDepth += 1
            for _ in len(queue):
                node = queue.popleft()

                if not node.left and not node.right:
                    return minDepth #易错点

                if node.left:
                    queue.append(node.left)
                #else: 
                    #return minDepth
                
                if node.right:
                    queue.append(node.right)
                #else:
                    #return minDepth
                
        return minDepth
