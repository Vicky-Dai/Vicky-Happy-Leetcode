import collections
from TreeNode import TreeNode

class Solution:
    def connect(self, root: 'TreeNode') -> 'TreeNode':
        if not root:
            return root
        
        queue = collections.deque([root])
        
        while queue: #层序遍历 每次处理一层
            level_size = len(queue)
            prev = None #初始化 prev 为 None，用来追踪当前层的前一个节点。
            
            for i in range(level_size):
                node = queue.popleft()
                
                if prev: #如果prev不为空 指向下一个
                    prev.next = node  
                
                prev = node
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
        
        return root
    #在表示二叉树或其他树形结构时，# 通常用来表示“空”或“不存在”的节点。这是一种常见的表示方法，尤其是在序列化树结构时，以便能够准确地重建树结构或清晰地展示树的层级结构。
#所以看到题目出现#不要奇怪