#递归法
from TreeNode import TreeNode  #在同一目录下不需要写路径 我把TreeNode文件也放在了BT文件夹下

class Solution:
    def isSymmetric(self, root: TreeNode) ->bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
    
    def compare(self, left,right):
        #首先排除空节点的情况 一定注意顺序 贸然直入如果为空会出错
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left.val != right.val: return False
        
        #此时就是：左右节点都不为空，且数值相同的情况
        #此时才做递归，做下一层的判断
        outside = self.compare(left.left, right.right) #左子树：左、 右子树：右
        inside = self.compare(left.right, right.left) #左子树：右、 右子树：左
        isSame = outside and inside #左子树：中、 右子树：中 （逻辑处理）
        return isSame
    

#迭代法 队列
import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left) #将左子树头结点加入队列
        queue.append(root.right) #将右子树头结点加入队列
        while queue: #接下来就要判断这这两个树是否相互翻转
            leftNode = queue.popleft() #更新leftnode rightnode    while后面是QUEUE 尽管每次比较和加入的数量不等 只要加入的还没消耗完就继续
            rightNode = queue.popleft()
            if not leftNode and not rightNode: #左节点为空、右节点为空，此时说明是对称的
                continue
            
            #左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left) #加入左节点左孩子
            queue.append(rightNode.right) #加入右节点右孩子
            queue.append(leftNode.right) #加入左节点右孩子
            queue.append(rightNode.left) #加入右节点左孩子
        return True 
        