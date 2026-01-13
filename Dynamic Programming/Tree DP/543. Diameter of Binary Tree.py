class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0  # height = 0

            left_h = dfs(node.left)
            right_h = dfs(node.right)

            # 更新直径
            self.ans = max(self.ans, left_h + right_h)

            # 当前节点的高度
            return 1 + max(left_h, right_h)

        dfs(root)
        return self.ans
