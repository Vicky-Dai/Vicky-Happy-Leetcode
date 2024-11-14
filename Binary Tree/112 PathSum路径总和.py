from TreeNode import TreeNode
class Solution:
    def hasPathSum(self, root: TreeNode, sum:int) -> bool:
        if not root: 
            return None
        return self.traversal(root, sum-root.val)#中节点直接在传入的时候就处理逻辑了，所以本道题前中后序都可以，因为在递归里根本没有中
    #主函数 考虑整体的特殊情况

    def traversal(self, cur:TreeNode, count:int) -> bool:
        #递归结束的条件，如果想不清楚，直接想找到最后一层是什么样子的，它控制着递归的终止，不会无限递归下去，但是递归返回的过程依赖于递归体中的 return 语句。
        if not cur.left and not cur.right and count ==0:
            return True
        if not cur.left and not cur.right:
            return False
        
        if cur.left:
            count -= cur.left.val
            if self.traversal(cur.left, count):
                return True
            count += cur.left.val #回溯，前面if那里为False的话，说明没找到点，那么回溯回去，回到上一个交叉点然后向右。

        if cur.right:
            count -= cur.right.val
            if self.traversal(cur.right, count): 
                return True
            count += cur.right.val

        return False