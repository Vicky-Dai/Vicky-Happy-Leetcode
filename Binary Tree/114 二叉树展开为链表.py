#前序遍历 重新构建 利用数组 in place不一定要当场构建
# 真正的 in place 后序遍历，从最底层构建
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
        

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        preorderList = list()

        def preorderTraversal(root: TreeNode):
            if root:
                preorderList.append(root)
                preorderTraversal(root.left)
                preorderTraversal(root.right)
        
        preorderTraversal(root)
        size = len(preorderList)
        for i in range(1, size):
            prev, curr = preorderList[i - 1], preorderList[i]
            prev.left = None
            prev.right = curr

