#构造二叉搜索树的统一框架思路就是先取中间节点，然后分别给左右子树找中间节点，再分配左右，所以就是前序遍历
#只要涉及到切割就要遵循循环不变量原则 此题采用左闭右闭
"""时间复杂度：O（n）  """
from TreeNode import TreeNode

def traversal(self, nums: list[int], left: int, right: int) -> TreeNode:
    if left < right: #终止
        return None
    
    #单层循环
    #中
    mid = left + (right - left)//2
    node = TreeNode(nums[mid], None)

    #左 这道题直接在原数组上面切就行 所以似乎就不用slicing
    node.left = traversal(nums, left, mid-1)
    node.right = traversal(nums, mid+1, right)  #这里传入，上面有个left，下面有个right，你可以想象你自己在做具体例子的时候，对他们的总结就是，把剩下的左边到中间之前的部分在切成中间左边右边，所以左边可以直接用left；右侧同理

    return node
    

   
def sortedArrayToBST(self, nums: list[int]) -> TreeNode:
    root = traversal(nums, 0, len(nums)-1 )
    