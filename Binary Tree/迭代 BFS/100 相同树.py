from TreeNode import TreeNode 

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        
        elif not p or not q: 
            return False
        
        elif p.val != q.val: return False

        return self.isSame(p.left, q.left) and self.isSameTree(p.right, q.right)
