class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        countA = 0
        countB = 0
        while headA:  # 原来写的 while headA.next:  计算长度不要用next
            countA += 1
        while headB:
            countB += 1

        if countB<countA:
            temp = headA
            headA = headB
            headB = temp
        for i in range(countB-countA):
            headB=headB.next
  '''      for i in range(countA-1):
            if headA == headB:
                return headA.val
                headA = headA.next
                headB = headB.next
        else:
            return null'''   #这里else是外层的 但if else配对没法这么用

        while headA.next and headB.next:
    
                
            

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
headA = create_list([4, 1, 8,  4, 5])
headB = create_list([5, 0, 1, 8,  4, 5])
result = solution.getIntersectionNode(headA, headB)
print("Intersect at:")
print_list(result)    