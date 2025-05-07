# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

#
# Note: 类名、方法名、参数名已经指定，请勿修改
#
#
# 
# @param root TreeNode类  二叉树数组
# @return int整型二维数组
#
from collections import deque 
class Solution:
    def levelNode(self, root) :
        # write code here
        queue = deque()
        queue.append(root)
        new_queue =[]
        res =[[root.val]]
        while queue:
            cur = queue.popleft()
            if cur.left:
                new_queue.append(cur.left)
            if cur.right:
                new_queue.append(cur.right)
            if not queue:
                cur_res = []
                for node in new_queue:
                    cur_res.append(node.val)
                res.append(cur_res[:])
                queue.extend(new_queue)
                new_queue = []
        return res