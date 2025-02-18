class Solution:
    def flatten(self, root) -> None:
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right

        root.left = None
        root.right = left

        # 找到新的右子树的最右边的节点（原来的左子树）然后把右子树挂上去
        p = root
        while p.right is not None:
            p = p.right
        p.right = right
        
