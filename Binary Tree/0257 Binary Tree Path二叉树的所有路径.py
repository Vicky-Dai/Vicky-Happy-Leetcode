from TreeNode import TreeNode

class Solution:
    def traversal(self, cur, path, result):
        path.append(cur.val) #中
        if not cur.left and not cur.right: #递归条件 到达叶子节点 也就是说走完了当前的path 该记录了
            sPath = '->'.join(map(str, path))
            result.append(sPath)
            
        #递归与回溯，叶子节点层做完记录操作了之后return 回到上一层，pop之前的节点，一层层pop，直到剩下的顶端作为下次一开始的头    
        if cur.left:   
            self.traversal(cur.left, path, result)
            path.pop()
        if cur.right:
            self.traversal(cur.right, path, result)
            path.pop

    def binaryTreePaths(self, root):
        result = []  #就定义一次  所以必须放在主函数里面
        path = []
        if not root:
            return result
        self.traversal(root, path, result)
        return result
    #什么时候需要主函数？  内容需要判断和调用的时候，想要集中递归逻辑