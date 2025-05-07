class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None

'''class Solution:
    def deLastN(self, n:int, head:ListNode) -> ListNode:
        left = head
        right = head.next

        for i in range(n-1):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return head''' #原来写的 没有使用头节点，要注意链表要考虑一个头节点的特殊情况，如果val刚好等于长度，那么rear就会变成none，而rear.next会报错

class Solution:
    def removeNthFromEnd(self, head: ListNode, n:int) -> ListNode:
        dummy_head = ListNode(0, head) #注意这里初始化一定要head不然出错
        f, s = dummy_head, dummy_head

        for i in range(n+1): #！！！！！！！！这里是n+1
            f = f.next

        while f:
            s = s.next
            f = f.next
        s.next = s.next.next

        return dummy_head.next
            
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
head = create_list([1, 2])
val = 2
new_head = solution.removeNthFromEnd(val, head)
print("Test Case 1 Result:")
print_list(new_head)    