# Definition
class ListNode:
    def _int_ (self, val: int, next = None):
        self.val = val
        self.next = next

def get(self, head:None, index:int):
    cur = head
    for i in range(index):
        cur = cur.next
        
