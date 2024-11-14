#递归 
from TreeNode import TreeNode

class Solution:
    def searchBST(self, root:TreeNode, val:int) -> TreeNode:
        if root == None or root.val == val:
            return root
        
        if val < root.val: root = self.searchBST(root.left, val)
        elif val > root.val: root = self.searchBST(root.right, val)
        return root
