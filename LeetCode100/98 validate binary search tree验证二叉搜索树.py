#BST中序遍历是有序的 利用递增转换成数组
from TreeNode import TreeNode

class Solution:
    def __init__(self):
        self.vec = []

    def traversal(self, root):
        if root is None:
            return
        self.traversal(root.left)#左边
        self.vec.append(root.val)#中
        self.traversal(root.right)#右

    def isValidBST(self, root):
        self.vec = []
        self.traversal(root)
        for i in range(1, len(self.vec)):
            if self.vec[i] <= self.vec[i-1]:
                return False
        return True


class Solution:
    def __init__(self):
        self.maxVal = float('-inf')

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #最重要的是不要复杂化，想象一下如果只是一个数组怎么判断它递增，类比到二叉树利用它的特性，中序可以递增输出
        if not root:
            return True #空的也是二叉搜索树
        left =  self.isValidBST(root.left)
        
        if self.maxVal < root.val:
            self.maxVal = root.val
        else:
            return False
        right = self.isValidBST(root.right)
       
        return left and right #左右两边都符合二叉搜索树,return True  跟700比较，700是left right都有return，这是因为700是只要找到符合的值就直接返回，而这道题是要判断整个二叉树，没有明确返回“值”，只有False 和True
    
    #想清楚怎么保证按顺序比较的，是因为中序遍历，实际上在向左地柜的时候，实际上是先递归到最左边，再和之前保存的maxVal比较的，因此可行