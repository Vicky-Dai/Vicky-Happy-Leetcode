#前序遍历 重新构建 利用数组 in place不一定要当场构建
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