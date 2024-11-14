class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == q or root == p or root is None:
            return root #前两种是一种情况 就是遇到需要找的节点，就往上返（注意这里里面还有两种情况，一种就是两个有共同的祖先，一种是两个的其中一个就是公共祖先，都包含在这里）
        #第二种情况是root 为None， 遍历结束了，这时候返回root就是返回None

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left is None and right is not None: #两边找到了我们的p和q
            return root
        elif left is None and right is not None: #返回那个底下有我们找到的
            return right
        elif left is not None and right is None:
            return left
        
        else:
            return None #左右都是空的情况下就返回None 因为什么也没找到