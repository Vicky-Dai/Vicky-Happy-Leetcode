class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverselist(self, head: ListNode) -> ListNode: # 箭头返回这个忘记写了
       # pre = head
       #cur = head.next 我原来写的 因为没有处理好头节点导致 loop 死循环了 第一个节点指向第二个节点，第二个节点又指向第一个节点
       pre =None
       cur = head

       while cur:
           temp = cur.next
           cur.next = pre
           pre = cur
           cur = temp
       return pre
    