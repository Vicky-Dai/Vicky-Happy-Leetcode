#迭代 利用特性
from TreeNode import TreeNode

class Solution:
    def searchBST(self, root:TreeNode, val:int) -> TreeNode:
        while root:
            if val < root.val: root.left
            elif val > root.val: root.right
            else: return root

        return root
    


        