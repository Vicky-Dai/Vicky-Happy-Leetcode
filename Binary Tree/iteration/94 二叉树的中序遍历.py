from TreeNode import TreeNode 

class Solution:
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        res = []
        stack = [] #指针负责遍历访问节点，栈用来处理节点上的元素(包括遍历之后存储，弹出储存进res)
        cur = root #把root的变量值 也就是整块地址给了cur  
        while cur or stack:  
            #先迭代访问最底层的左子树节点
            if cur:
                stack.append(cur)
                cur = cur.left  
            else: #当前节点若为左null，作为空第一次弹出父节点，进入else，走到右null作为第二次null，弹出爷爷
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
