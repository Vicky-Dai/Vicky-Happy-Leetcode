# 迭代法 层序遍历
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = collections.deque([root])
        right_view = []

        while queue:
            level_size = len(queue)
            
            for i in range(level_size):
                node = queue.popleft()
                
                if i == level_size - 1:
                    right_view.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return right_view