#递归法BFS模板 也是102题的解法
import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]):
        if not root:
            return []
        levels = []
        def traverse(node, level):
            if not node:
                return
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)

        traverse(root, 0)
        return levels
