from typing import Optional

#Definition for singly-linked list.
class ListNode: #这个 ListNode 类定义的是一个单链表的节点
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # 创建虚拟头部节点以简化删除过程
        dummy_head = ListNode(next = head) # 用构造函数构造一个虚拟头节点
        
        # 遍历列表并删除值为val的节点
        current = dummy_head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next
    #为什么要返回 dummy_head.next
#由于我们使用了虚拟头节点 dummy_head，链表的实际头节点可能会被删除（如果它的值等于 val），或者保持不变。因此，我们需要返回虚拟头节点的 next，它始终指向实际链表的头节点。
    
solution = Solution()

# 创建链表的辅助函数  
# 总结来说，create_list 函数将一个列表转换为一个链表，并返回链表的头节点。这个函数在处理链表相关的操作时非常有用，比如在测试链表操作的代码时，可以方便地创建链表。
def create_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# 打印链表的辅助函数
def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example 1:
head = create_list([1, 2, 6, 3, 4, 5, 6])
val = 6
new_head = solution.removeElements(head, val)
print("Test Case 1 Result:")
print_list(new_head) 
