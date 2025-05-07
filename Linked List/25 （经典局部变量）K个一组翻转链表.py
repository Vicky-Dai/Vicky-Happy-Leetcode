class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail: # ！！！！！！！！！！
            nex = p.next
            p.next = prev # 从用例来讲，这里已经实现了1指向4了 （下面出去之后还会再做一次 所以那一句代码可有可无 见下面！
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0, head) # 记得连到head上！不然后面的tail.next = nex会报错！
        pre = hair # pre在 while 外面，作用域是整个函数体 这意味着它在整个 reverseKGroup() 函数运行期间都存在。

        while head:
            tail = pre # 重置pre！ ## ✅ 这里声明了“新的局部变量 tail”
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next # ？？？？？ 如果剩余部分长度小于 k，直接返回
            nex = tail.next

            head, tail = self.reverse(head, tail) # reverse函数里面的变量只在这个函数作用域里面有效，所以要返回回来接住才能改变
            # 这句话虽然是“覆盖了当前函数中的 tail”，但是只影响这一轮 while 中的 tail 变量绑定。也就是说，下一轮while中的tail变量还是原来的tail，这也是为什么每次while循环开始要重新设置tail的位置
            # 但是为什么pre就保留了下来呢？？ pre 保留了下来，是因为它是 while 循环外定义的局部变量，但它绑定的是一个链表节点对象，对象没有丢，引用一直在。

            # 下面把子链表重新接回原链表
            pre.next = head
            tail.next = nex # 这里的 tail.next = nex 是为了把翻转好的子链表的尾部接回原链表 也就是可有可无的地方！
            pre = tail  # 我们刚刚把 k 个节点反转了（比如 3 -> 2 -> 1），现在新的前缀节点 pre 应该更新成这一段的新末尾
            head = tail.next # 我们要继续处理接下来的节点，也就是当前段的下一个节点（原来的第 k+1 个）
        
        return hair.next

""" 经典用例：输入：head = [1,2,3,4,5], k = 3
输出：[3,2,1,4,5]   """

""" 大多数时候，代码不会写，并不是代码的问题，而是现实中进行的逻辑没搞清楚
 p 是当前节点

prev 是已经翻转好的那部分的“前面”

nex 是暂存下一个节点（防止链断）"""


""" def foo():
    a = 1
    print("Before:", a)
    bar(a)
    print("After:", a)

def bar(x):
    x = 100  # 这个赋值不会改变 foo() 里的 a

foo() """

# 纯代码版
class Solution:
    # 翻转一个子链表，并且返回新的头与尾
    def reverse(self, head: ListNode, tail: ListNode):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        hair = ListNode(0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            # 查看剩余部分长度是否大于等于 k
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            # 把子链表重新接回原链表
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        
        return hair.next

# 我自己的写法

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        hair = ListNode(0, head)
        pre, tail = hair, hair
        while head:
            # tail = pre 因为tail在外面定义的（作用域是整个函数），所以每次下面tail赋值了，它的值会被覆盖掉
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next

    def reverse(self, head, tail):
        last = tail.next
        p = head
        while last != tail:
            nex = p.next
            p.next = last
            last = p
            p = nex
        return tail, head