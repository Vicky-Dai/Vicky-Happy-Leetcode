class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return []
        self.sum = 0
        self.traverse(root)
        return root
    
    def traverse(self, root):
        if not root:
            return 
        self.traverse(root.right)
        self.sum += root.val
        root.val = self.sum
        self.traverse(root.left)
