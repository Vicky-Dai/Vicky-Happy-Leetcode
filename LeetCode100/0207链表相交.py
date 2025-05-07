class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        countA, countB = 0, 0    #不能动headA
        curA = headA
        curB = headB
        while curA:  # 原来写的 while headA.next:  计算长度不要用next
            countA += 1
            curA = curA.next
        while curB:
            countB += 1
            curB = curB.next

        curA, curB = headA, headB  #想清楚为什么一定要写这个 因为下面if不走的话 cur还得回到head 

        if countB<countA:
            curA, curB = curB, curA
            countA, countB = countB, countA   #注意一个这里是交换语法
            
        for i in range(countB-countA):
            curB = curB.next


        while curA: #少一个行不行
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
    
                
            

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
        print(current.val, end=" -> ") #**`end`**: 打印结束时的字符（默认为换行符 `\n`）。
        current = current.next
    print("None")

# Helper function to attach a node at the end of a list #这个是我没想到的！！
def attach_list(head, node):
    current = head
    while current.next:
        current = current.next  #使用 while 循环遍历链表，直到 current.next 为 None，即找到链表的最后一个节点。
    current.next = node
    
#测试用例1
# Common part
common = create_list([8, 4, 5])

# List A
headA = create_list([4, 1])
attach_list(headA, common)

# List B
headB = create_list([5, 0, 1])
attach_list(headB, common)
result = solution.getIntersectionNode(headA, headB)
print("Intersect at:")
if result:
    print(result.val) 
else:
    print("No intersection")
   #例如，如果链表 A 和链表 B 都包含值 8，但位于不同的节点中，则无法确定交点节点的具体位置。
   #所以要在函数中获取节点，打印的时候再取首值