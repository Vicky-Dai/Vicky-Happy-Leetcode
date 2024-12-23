#堆的操作 O(LOGK)
#总时间复杂度是O(nlogk)

from heapq import heappush, heappop
from typing import List, Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # 定义比较函数以支持堆排序
    def __lt__(self, other):
        return self.val < other.val

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    min_heap = []
    
    # 初始化堆，把每个链表的头节点加入堆中
    for i, node in enumerate(lists):
        if node:  # 如果链表不为空
            heappush(min_heap, (node.val, i, node)) #heapq 模块中的 heappush 方法将元素加入到堆中 heappush(heap, item) 将 item 插入到 heap 中，同时维持堆的性质（小顶堆或大顶堆）。
    
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