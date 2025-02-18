import collections
from TreeNode import TreeNode
from typing import Optional
from collections import deque

class Solution: 
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        #Optional[TreeNode]：表示一个变量可以是 TreeNode 类型，也可以是 None。这是为了允许这个变量在某些情况下没有值（即为空），同时也可以有一个 TreeNode 类型的值。
        if not root:
            return []
        queue = collections.deque([root]) #collections python自带标准库，双端队列
        # 这一行代码是用来初始化一个双端队列（deque）并将根节点添加到其中。创建一个双端队列（deque）来作为辅助队列，用于存储节点
        result = []# 用于存储最终结果的列表

        while queue:# 当队列不为空时，继续遍历 直到最后一层也被挨个popleft之后 每个节点的左右节点左右子孩子都是None
            level = [] # 遍历当前层的所有节点
            for _ in range(len(queue)): # 遍历当前层的所有节点
                cur = queue.popleft()  # 从队列中取出一个节点
                level.append(cur.val) # 将节点的值添加到当前层的结果列表中
                if cur.left:  # 如果当前节点有左子节点，将左子节点添加到队列中
                    queue.append(cur.left)
                if cur.right: # 如果当前节点有右子节点，将右子节点添加到队列中
                    queue.append(cur.right)
            result.append(level)   # 将当前层的结果添加到最终结果列表中
        return result
    

