from TreeNode import TreeNode

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.value = 0
        root = self.traversal (root)
        return root  #记得返回root
     
    def traversal(self, cur):
        #终止条件
        self.value = 0
        if not cur:
            return None
        
        #右
        cur.right = self.traversal(cur.right) #类方法记得加self.

        #中
        self.value = self.value + cur.val
        cur.val = self.value

        #左
        cur.left = self.traversal(cur.left)

        return cur
#以上是我自己写的代码

#本题还有双指针操作
#二叉搜索树的众数
#二叉搜索树中的最小绝对差
#本题还是迭代法模板题
#递归函数有没有返回值取决于什么？