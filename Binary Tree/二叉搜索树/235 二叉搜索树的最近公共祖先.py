from TreeNode import TreeNode

class Solution:
    def traversal(self, cur, p, q) -> TreeNode:
        if (cur == None):
            return None
        if cur.val > p.val and cur.val > q.val:           # 左
            left = self.traversal(cur.left, p, q)
            if left is not None:
                return left


        if cur.val < p.val and cur.val < q.val:           # 右
            right = self.traversal(cur.right, p, q)
            if right is not None:
                return right
            
        return cur #找到了就一路返回
        
    
    def lowestCommonAncestor(self, root, p, q):
        return self.traveral(root, p, q)