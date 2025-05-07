#这段代码通过对每个节点都执行“中间点”的判断，有效涵盖了所有可能；
""" 时间复杂度 O(n) 空间复杂度 O(h) h为树的高度"""

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 1
        def depth(node):
            # 访问到空节点了，返回0
            if not node:
                return 0
            # 左儿子为根的子树的深度
            L = depth(node.left)
            # 右儿子为根的子树的深度
            R = depth(node.right)
            # 计算d_node即L+R+1 并更新ans
            self.ans = max(self.ans, L + R + 1)
            # 返回该节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1



class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root.left and not root.right:
            return 0
        self.maxdepth = float('-inf')
        self.findDepth(root.left, 0)
        left = self.maxdepth
        self.maxdepth = float('-inf')
        self.findDepth(root.right, 0)
        right = self.maxdepth

        return left + right
    
    def findDepth(self, root, depth):
        if not root:
            self.maxdepth = max(self.maxdepth, depth)
            return
        depth += 1
        self.findDepth(root.left, depth)
        self.findDepth(root.right, depth)
        return

        