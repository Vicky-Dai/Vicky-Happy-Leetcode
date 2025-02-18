class Solution:
    # 存储 postorder 中值到索引的映射
    valToIndex = dict()

    def constructFromPrePost(self, preorder, postorder):
        for i in range(len(postorder)):
            self.valToIndex[postorder[i]] = i
        return self.build(preorder, 0, len(preorder) - 1,
                          postorder, 0, len(postorder) - 1)

    # 定义：根据 preorder[preStart..preEnd] 和 postorder[postStart..postEnd]
    # 构建二叉树，并返回根节点。
    def build(self, preorder, preStart, preEnd,
              postorder, postStart, postEnd):
        if preStart > preEnd:
            return None
        if preStart == preEnd:
            return TreeNode(preorder[preStart])

        # root 节点对应的值就是前序遍历数组的第一个元素
        rootVal = preorder[preStart]
        # root.left 的值是前序遍历第二个元素
        # 通过前序和后序遍历构造二叉树的关键在于通过左子树的根节点
        # 确定 preorder 和 postorder 中左右子树的元素区间
        leftRootVal = preorder[preStart + 1]
        # leftRootVal 在后序遍历数组中的索引
        index = self.valToIndex[leftRootVal]
        # 左子树的元素个数
        leftSize = index - postStart + 1
     
        # 先构造出当前根节点
        root = TreeNode(rootVal) 
        # 递归构造左右子树
        # 根据左子树的根节点索引和元素个数推导左右子树的索引边界
        root.left = self.build(preorder, preStart + 1, preStart + leftSize,
                               postorder, postStart, index)
        root.right = self.build(preorder, preStart + leftSize + 1, preEnd,
                                postorder, index + 1, postEnd - 1)

        return root