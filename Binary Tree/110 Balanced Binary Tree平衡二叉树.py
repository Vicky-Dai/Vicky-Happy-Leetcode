#平衡二叉树要求它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。
#求高度必须后序遍历，因为要先求左右子树的高度，然后再求根节点的高度，这样才能判断左右子树是否平衡
#对比104可以用前序是因为求得是根节点的高度，不需要左右子树的高度
#然而，具体到个别的叶子节点，它的左右子树的高度差可能大于1，但是它的父节点的左右子树的高度差却不大于1，所以就可能出现误判。
""" 时间复杂度：O(n)，每个节点被访问一次。
空间复杂度：O(h)，其中 h 是树的高度，最坏情况下是 O(n)（即树为链状） """
from TreeNode import TreeNode

class Solution:
    def isBalanced(self, root:'TreeNode') -> bool:  #递归参数
        if self.getheight(root) != -1: #递归终止条件
            return True
        else:
            return False

    def get_height(self, root: TreeNode) -> int:
        #递归体 
        if not root:
            return 0
        #左
        if (left_height := self.getheight(root.left)) == -1: #海象操作符：调用self.get_height(root.left)方法，并将返回值赋给left_height变量。使得能够在表达式赋值
            return -1
        #右
        if (right_height := self.get_height(root.right)) == -1:
            return -1
        #中
        if abs(left_height - right_height) > 1:
            return -1
        else:
            return 1 + max(left_height, right_height)