class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def roundList(self, head:ListNode) -> int:
        fast, slow = head, head
        while fast and fast.next: #循环目标指导循环条件设置，而不要直接作为循环条件
            fast = fast.next.next
            slow = slow.next
            # If there is a cycle, the slow and fast pointers will eventually meet
            
            #找到环之后找入口， 让头和遇到点同时走，遇到的就是入口  数学分析
            if fast == slow: 
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
#fast = 2slow 
        return None
                
        
#（版本二）集合法
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        
        while head:
            if head in visited:
                return head
            visited.add(head)
            head = head.next
        
        return None
