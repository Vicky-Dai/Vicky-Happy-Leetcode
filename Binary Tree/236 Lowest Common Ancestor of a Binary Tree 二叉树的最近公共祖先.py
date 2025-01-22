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
        
""" 在有序树里，如果判断一个节点的左子树里有p，右子树里有q呢？

因为是有序树，所以 如果 中间节点是 q 和 p 的公共祖先，那么 中节点的数组 一定是在 [p, q]区间的。即 中节点 > p && 中节点 < q 或者 中节点 > q && 中节点 < p。

那么只要从上到下去遍历，遇到 cur节点是数值在[p, q]区间中则一定可以说明该节点cur就是p 和 q的公共祖先。 那问题来了，一定是最近公共祖先吗？
此时节点5是不是最近公共祖先？ 如果 从节点5继续向左遍历，那么将错过成为p的祖先， 如果从节点5继续向右遍历则错过成为q的祖先。
所以当我们从上向下去递归遍历，第一次遇到 cur节点是数值在[q, p]区间中，那么cur就是 q和p的最近公共祖先。 """