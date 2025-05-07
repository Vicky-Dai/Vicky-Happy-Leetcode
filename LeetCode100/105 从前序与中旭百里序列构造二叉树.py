from TreeNode import TreeNode
class Solution:
    def buildTree(self, inorder:list[int], preorder:list[int]) -> TreeNode:
        #特殊情况讨论 也是递归终止条件
        if not preorder:
            return None
        
        #第二步：前序遍历的第一个就是当前的中间节点
        root_val = preorder[0]
        root = TreeNode(root_val)

        #第三步：用找到的中间节点作为切割点，在前序遍历找到它
        separator_idx = inorder.index(root_val)

        #第四部：切割inorder数组，得到Inorder数组的左右半边
        inorder_left = inorder[:separator_idx]
        inorder_right =  inorder[separator_idx + 1:]


        #第五步：用inorder切割的数组长度，来切割还连在一起的postorder
        preorder_left = preorder[ 1:len(inorder_left)+1 ]
        preorder_right = preorder_left[len(inorder_left)+1:]

        #第六步：递归
        root.left = self.buildTree(inorder_left, preorder_left)
        root.right = self.buildTree(inorder_right, preorder_right)

        #第七步：递归返回逻辑以及最终结果返回
        return root
