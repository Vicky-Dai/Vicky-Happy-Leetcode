# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        dummy_head = ListNode(-1)
        p = dummy_head
        curA, curB = list1, list2
        while curA and curB:
            if curA.val < curB.val:
                p.next = curA
                curA = curA.next
                p = p.next
            else:
                p.next = curB
                curB = curB.next
                p = p.next
        if not curA:
            p.next = curB

        if not curB:
            p.next = curA
        return dummy_head.next