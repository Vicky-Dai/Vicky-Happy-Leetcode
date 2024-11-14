#终止条件一定是写在单层递归体前面，所以在思考逻辑的时候，一定是每一层新的口袋口子开的时候，用什么条件能让这个口子立刻堵住
#也就是说一定要分清开头和结尾，第一个重复的地方就是开始，而递归终止条件仅仅指开到最后一个不能开的口子缝上，但是递归函数彻底结束式整个缝合彻底结束，也就是最上层的口子缝合好的时候

from TreeNode import TreeNode
class Solution:
    def buildTree(self, inorder:list[int], postorder:list[int]) -> TreeNode:
        #第一步：如果数组大小为零的话，说明是空节点了。 特殊情况讨论 也是递归终止条件
        if not postorder:
            return None
        
        #第二步：后序遍历的最后一个就是当前的中间节点
        root_val = postorder[-1]
        root = TreeNode(root_val)

        #第三步：用找到的中间节点作为切割点，在inorder遍历找到它 index()方法
        separator_idx = inorder.index(root_val)

        #第四部：切割inorder数组，得到Inorder数组的左右半边
        inorder_left = inorder[:separator_idx]
        inorder_right =  inorder[separator_idx + 1:]


        #第五步：用inorder切割的数组长度，来切割还连在一起的postorder
        postorder_left = postorder[:len(inorder_left) -1 ]
        postorder_right = postorder_left[len(inorder_left):len(postorder)-1]

        #第六步：递归
        root.left = self.buildTree(inorder_left, postorder_left)
        root.right = self.buildTree(inorder_right, postorder_right)

        #第七步：递归返回逻辑以及最终结果返回
        return root

