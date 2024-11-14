#二叉搜索树中插入任何节点都可以在叶子节点找到位置 所以相对来说就会简单很多 虽然本身插入之后位置不是唯一的 结构也不是唯一的 但是那样去做就复杂了
from TreeNode import TreeNode

class Solution:
    def __init__(self):
        self.parent = None #干嘛用

    def traversal(self, cur, val):
        if cur is None: #终止条件 比如要插入0 一直想左找找找 直到找到叶子结点下一个位置cur为0，那就找到地方了
            node = TreeNode(val)
            if val > self.parent.val:
                self.parent.right = node
            else:
                self.parent.left = node
            return
        
        self.parent = cur
        if cur.val > val:
            self.traversal(cur.left, val)

        if cur.val < val:
            self.traversal(cur.right, val)

    def insertIntoBST(self, root, val): #这个的本质其实是 root = insertIntoBST(self, root, val) 对吗
        self.parent = TreeNode(0)
        if root is None:
            return TreeNode(val)
        self.traversal(root, val)
        return root
    
    #实例化的过程 self全部被替代成实例 比如solution
   

#优化版本二
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None or root.val == val:  #root.val == val: 这里是干什么的？ 忽略插入了吗
            return TreeNode(val)
        elif root.val > val:
            if root.left is None:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        elif root.val < val:
            if root.right is None:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        return root
    
#优化版本三
class Solution:
    def insertIntoBST(self, root, val):
        if root is None:
            node = TreeNode(val)
            return node

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)

        return root
    