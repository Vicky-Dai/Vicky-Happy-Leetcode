""" * """
#堆的操作 O(LOGK)
#总时间复杂度是O(nlogk)
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        import heapq
        min_heap = [] #！！！用数组实现
        for i, node in enumerate(lists):
            if node: # ！！！！
                heappush(min_heap, (node.val, i, node))

        dummy = ListNode(0)
        current = dummy

        while min_heap:
            val, i, node = heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))
        return dummy.next
    
    
    
from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 定义比较函数以支持堆排序
    def __lt__(self, other):
        return self.val < other.val # 这里重载了节点比较方法，heappush(min_heap, (node.val, i, node)) 比较到最后一步比较不出来的时候，需要这样一个方法来解决

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    min_heap = []
    
    # 初始化堆，把每个链表的头节点加入堆中
    for i, node in enumerate(lists):
        if node:  # 如果链表不为空
            heappush(min_heap, (node.val, i, node)) #heapq 模块中的 heappush 方法将元素加入到堆中 heappush(heap, item) 将 item 插入到 heap 中，同时维持堆的性质（小顶堆或大顶堆）。 自动维持的是小顶堆，如果要大顶堆，需要把比较参数取负数
    
    # 定义一个哑节点，方便操作
    dummy = ListNode(0)
    current = dummy
    
    # 从堆中不断取出最小值，加入结果链表
    while min_heap:
        val, i, node = heappop(min_heap)  # 取出堆顶
        current.next = node  # 链接到结果链表
        current = current.next  # 移动指针
        
        if node.next:  # 如果当前节点有后续节点，把后续节点加入堆
            heappush(min_heap, (node.next.val, i, node.next)) #将链表的下一个节点加入堆，以确保堆中始终包含来自每个链表的未处理节点
    
    return dummy.next


#最小堆heapq 会自动维护大小顺序。无论你对堆执行插入 (heappush) 还是删除最小值 (heappop) 操作，heapq 都会确保堆的结构始终符合 小顶堆 的性质， 取出顺序是从小到大 

""" Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
这里面是用数组表示多个链表，lists: List[Optional[ListNode] 这个的意思是：该数组是一个包含多个链表头节点的数组，每个元素代表一个链表的头节点 """


""" 1. 多路归并的思考
合并两个有序链表是常见的链表操作，时间复杂度是 O(N)，其中 N 是两个链表的总节点数。
但是，如果我们要合并 k 个有序链表，一个接一个地合并，最坏情况下的时间复杂度是 O(kN)，效率不够高。
思路：能否像合并排序一样，分而治之，逐个合并，或者借助更高效的数据结构？ """

""" 2. 借助堆（优先队列）进行最小元素的选择
堆是一种特别适合处理“动态选择最小或最大元素”的数据结构。
如果我们把每个链表的头节点都放入一个最小堆中，那么堆顶元素始终是当前所有节点中最小的那个节点。
每次从堆中取出最小元素，将其加入结果链表，并将取出节点的下一个节点继续放入堆中，保持堆的动态更新。 """

""" 每次操作堆的时间复杂度是 O(log k)，而合并的总节点数为 N，因此总复杂度为 O(N log k)，相比暴力法的 O(kN) 更高效。
即使 k 非常大（比如 1000 个链表），堆的操作复杂度依然较低，适合大规模链表合并问题。 """