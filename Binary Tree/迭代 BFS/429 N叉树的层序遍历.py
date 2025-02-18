"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
import collections
from TreeNode import TreeNode

class Solution:
    def levelOrder(self, root: 'TreeNode') -> list[list[int]]:
        if not root:
            return []
        result = []
        queue = collections.deque([root]) #[root] 是一个列表，表示要初始化的内容。

        while queue: #队列不为空就一直遍历
            level = [] #记录每一层

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    queue.append(child)
                
            result.append(level) #level是单个元素  再理解一下这里为什么level不需要加中括号 但是前面root需要

        return result
        