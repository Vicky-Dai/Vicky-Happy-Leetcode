class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # dp is a tuple, 0 means do not choose current vector, 1 means choose
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)

            left = dfs(node.left)
            right = dfs(node.right)

            # 1. 抢当前节点：左右孩子必须不抢
            rob_this = node.val + left[1] + right[1]

            # 2. 不抢当前节点：左右孩子可以抢也可以不抢，取最大
            not_rob_this = max(left) + max(right)

            return (rob_this, not_rob_this)

        return max(dfs(root))