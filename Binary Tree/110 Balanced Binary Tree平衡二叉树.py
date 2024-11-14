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