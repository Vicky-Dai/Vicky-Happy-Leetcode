

class ListNode:    #定义要会写
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteListNode(self, head: None, val: int): 
    dummyhead = Nodelist
    pre = dummyhead
    cur = head
    dummyhead.next = head

    while cur != None:
        if (cur.next == val):
            temp = cur.next
            cur = cur.next.next
            pre = temp
    return head   

