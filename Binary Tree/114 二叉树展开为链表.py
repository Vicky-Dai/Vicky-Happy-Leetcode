#前序遍历 重新构建 利用数组 in place不一定要当场构建
# 真正的 in place 后序遍历，从最底层构建

# 方法一： 递归（后序处理） 时间复杂度：O(n²) 空间复杂度：O(n)
class Solution:
    def flatten(self, root) -> None:
        if not root:
            return
        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left # !!!!!!!!!很有意思 先把左子树保存下来，右子树也保存下来。
        right = root.right # 把左子树挂到右边，并清空左子树。

        root.left = None
        root.right = left

        # 找到新的右子树的最右边的节点（原来的左子树）然后把右子树挂上去
        p = root
        while p.right is not None: #✅ 沿着新的右子树（原来的左子树）一直走到最右边，然后把原本的右子树挂上去。
            p = p.right
        p.right = right


# 方法二：递归（用全局变量记录上一个节点，逆序遍历） 时间复杂度：O(n) 空间复杂度：O(n)
class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.flatten(root.right)
        self.flatten(root.left)
        
        # 当前节点右指向上一个节点
        root.right = self.prev
        root.left = None
        self.prev = root

# 迭代（Morris Traversal） 用类似 Morris 遍历的方法，不用递归和栈，真正 O(1) 额外空间。

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        curr = root
        while curr:
            if curr.left:
                # 找到左子树的最右节点
                pre = curr.left
                while pre.right:
                    pre = pre.right
                pre.right = curr.right
                curr.right = curr.left
                curr.left = None
            curr = curr.right
