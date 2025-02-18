# 双指针 时间复杂度n
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
    


#递归实现 时间复杂度n
def reverse_list(root):
    # 递归终止条件：如果 root 或 root.next 为 None，说明已经到达链表末尾
    if root is None or root.next is None:
        return root
    
    # 递归调用，反转剩余链表
    temp = root.next
    node = reverse_list(root.next)
    
    # 断开 root 与后续节点的连接
    root.next = None
    
    # 将当前 root 的下一个节点指向 root，从而实现链表反转
    temp.next = root
    
    return node
