class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            left_path = right_path = 0

            # 如果左边值相同，可以接上
            if node.left and node.left.val == node.val:
                left_path = left + 1

            # 如果右边值相同，可以接上
            if node.right and node.right.val == node.val:
                right_path = right + 1

            # 更新答案：左右两条链合并成路径经过 node
            self.ans = max(self.ans, left_path + right_path)

            # 返回：只能返回最长的一条链给上层
            return max(left_path, right_path)

        dfs(root)
        return self.ans
