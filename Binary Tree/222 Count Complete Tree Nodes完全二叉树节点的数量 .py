#递归法 这个方法复杂度是O（n）会把所有的节点都遍历一边 和层序一样 当做普通二叉树来做
from TreeNode import TreeNode

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodesNum(root)
    
    def getNodesNum(self, cur):
        if not cur:
            return 0
        leftNum = self.getNodesNum(cur.left)#左 递归
        rightNum = self.getNodesNum(cur.right)
        treeNum = leftNum + rightNum + 1 #中
        #后续遍历
        return treeNum
    

#利用完全二叉树特性
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        count = 1
        left = root.left; right = root.right  #这里left right相当于两个指针
        while left and right:
            count += 1
            left = left.left; right = right.right
        if not left and not right: # 如果同时到底说明是满二叉树，反之则不是
            return 2**count -1
        return 1+self.countNodes(root.left) + self.countNodes(root.right)
    