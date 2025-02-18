import collections
from TreeNode import TreeNode


class Solution:
    def connect(self, root: 'TreeNode') -> TreeNode:
        if not root:
           return []
        queue = collections.deque([root]) #这里的 deque 是一个队列数据结构，专门用来实现广度优先搜索（BFS），并且它与链表不同，deque 并不是链表，而是可以从两端高效操作的队列。

        while queue:
            prev = None
            level_size = len(queue)

            for i in level_size:
                node= queue.popleft() #这里的 node 是树中的一个节点，而不是链表节点。
                if prev:
                    prev.next = node
                prev = node #if完成后会走到这里，当i==level_size-1的时候，prev等于最后一个节点。注意这里node本来就是来自queue，本来就是一个个节点，
#到了第三轮，即 i = 2，此时 node = node3 是当前层的最后一个节点。在这轮循环中，prev = node2，执行了 prev.next = node，也就是将 node2 的 next 指针指向了 node3。
#但是，循环结束后不会有更多节点来执行 prev.next = node，因此 node3 的 next 保持未赋值（即 None），也就是说，最后一个节点的 next 不会被更新，保持为 None。
#Node 类在定义时，next 指针的初始值是 None：
#class Node:
#    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
#        self.val = val
#        self.left = left
#        self.right = right
#        self.next = next  # 默认是 None
                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return root
    
    
    