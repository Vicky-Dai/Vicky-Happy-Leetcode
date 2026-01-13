class Solution:
    def distributeCoins(self, root):
        self.moves = 0

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            # 所有从左右孩子传过来的苹果，都要算移动次数
            self.moves += abs(left) + abs(right)

            # 返回当前子树的净贡献（多的给上面，少的从上面拿）
            return node.val + left + right - 1

        dfs(root)
        return self.moves