from TreeNode import TreeNode 

class Solution:
    def findBottomLeftValue(self, root: TreeNode):
        self.max_depth = float('-inf')
        self.result = None
        self.traversal(root, 0)
        return self.result
    
    def traversal(self, node, depth):
        if not node.left and not node.right: #遇到叶子结点，要统计一下最大的深度
            if depth > self.max_depth:
                self.max_dpth = depth
                self.result = node.val
            return
        #这里用的前序，但是其实本题中没有操作，所以用什么顺序都可以
        if node.left:
            depth += 1
            self.traversal(node.left, depth)
            depth -= 1

        if node.right:
            depth += 1
            self.traversal(node.right, depth)
            depth -= 1



