class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = tail = None  # 初始化头和尾指针
        carry = 0  # 进位初始化为0
        
        while l1 or l2:
            n1 = l1.val if l1 else 0  # 取 l1 当前位的值
            n2 = l2.val if l2 else 0  # 取 l2 当前位的值
            sum_val = n1 + n2 + carry  # 当前位相加 + 进位

            if not head:  
                head = tail = ListNode(sum_val % 10)  # 创建新节点作为头
            else:
                tail.next = ListNode(sum_val % 10)  # 追加新节点
                tail = tail.next  # 移动尾指针
            
            carry = sum_val // 10  # 计算进位
            
            # 移动 l1 和 l2 到下一位
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        if carry > 0:  # 处理最终进位
            tail.next = ListNode(carry)
        
        return head  # 返回链表的头节点
