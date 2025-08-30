#快慢指针
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        fast, slow = head, head
        while fast and fast.next: # 注意这个判断，一定要两个并且先fast 再next，否则会报错（AttributeError: 'NoneType' object has no attribute 'next'）
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        else: return False