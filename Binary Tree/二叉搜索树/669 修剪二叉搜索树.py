#这道题乍一看比450删除节点要难，因为要删除的更多，实际上要简单，这是为什么呢？
#因为它有清晰的目标范围，正是这个范围使得删除和替换逻辑变得统一且简单，具体来说就是，如果节点值小于 low，就完全忽略这个节点和它的左子树，直接返回修剪后的右子树。
#但是450删除就无法保证你这个目标节点到底处在什么样的一个位置，这就导致了删除之后的修复变得复杂，要分类讨论

#大的逻辑其实就是，1.找 2.处理  然后递归三部曲 这两块逻辑主要就是细化递归三部曲的递归体（但有的时候也能放到终止条件比如450）
#通常找要用递归来处理，那么处理节点要不要用递归呢？看一次能不能解决完，如果是确切的点如450，那么就一下解决掉，但是如果还不知道后面的情况如何，那只能用递归先占个位置，然后找找后面啥样，再返回来。

from TreeNode import TreeNode
class Solution:
    def trimBST(self, root: TreeNode, low: int, high: int) -> TreeNode:
        if root is None:
            return None #终止条件
        
        #这里的判断是用来删除的，
        if root.val < low:
            # 寻找符合区间 [low, high] 的节点 
            return self.trimBST(root.right, low, high) #
        if root.val > high:
            # 寻找符合区间 [low, high] 的节点 直接接上符合的来跳过不符合
            return self.trimBST(root.left, low, high)
        
        #找的过程 但是找的过程可以按规律简化，比如找到小的，左边扔掉，右边还要再找找；找到大的同理
        root.left = self.trimBST(root.left, low, high) # root.left 接入符合条件的左孩子
        root.right = self.trimBST(root.right, low, high)

        return root #每一层正常的的返回 