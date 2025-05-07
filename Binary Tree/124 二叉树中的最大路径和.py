# 递归 后序遍历 分治法 动态规划
# 怎么体现了一点动态规划：整棵树的最大路径和，取决于子树的最大路径和（例如左子树、右子树的最大贡献值），这是最优子结构的体现。
# 路径不能回头，不能分叉

class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain
            
            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)
        
            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)
   
        maxGain(root)
        return self.maxSum

# maxGain方法里面的最后三行是特别容易混的地方
# 1. priceNewpath = node.val + leftGain + rightGain
# 尝试把“当前节点作为路径的顶点”来看，看看能不能构成一个最大路径。
# 2. self.maxSum = max(self.maxSum, priceNewpath)
# 然后再用这条路径值去更新全局最大路径
# 3. return node.val + max(leftGain, rightGain)
# 告诉它的“父节点”：如果你要选我作为路径的一部分，我最多能为你贡献多少值？路径不能拐弯、不能走左右两边，只能从下面往上走一边。
# 总结：你自己作为路径终点时，可以左边+右边；但你给别人用时，只能选一边走上去。