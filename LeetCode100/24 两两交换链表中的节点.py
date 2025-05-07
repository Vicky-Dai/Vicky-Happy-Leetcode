class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    def exchangeTwo(self, head: listNode):
        pre = head
        cur = head.next
        while cur:
            temp = cur.next   #最好先确认temp  是一个不再战场里的人  否则变化会引起不必要的混乱
            cur.next = pre
            pre.next = temp
            pre = pre.next.next  #pre cur交换之后，继续找下一个的下一个，pre实际上指向了4  所以反转
            cur = cur.next.next #循环要求没写好容易导致寻址到不存在的地方引发attribute error
         return head  # 原来写的，head其实就是一个地址，已经被交换就改变了 """

class Solution:
    def exchangeTwo(self, head:ListNode) -> ListNode:
        dummyhead = ListNode(next=head)  #这个必须要用dummyhead叻 因为交换的是pre和cur本身 而不是箭头
        cur = dummyhead
        
        while cur.next and cur.next.next: #画图  顺序按照最终目的来 
            temp1 = cur.next
            temp2 = cur.next.next.next

            cur.next = cur.next.next
            cur.next.next = temp1
            temp1.next = temp2
            cur = cur.next.next
        return dummyhead.next
    
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


#测试用例1
head = create_list([1, 2, 6, 3, 4, 5, 6])
new_head = solution.exchangeTwo(head)
print("Test Case 1 Result:")
print_list(new_head)    


