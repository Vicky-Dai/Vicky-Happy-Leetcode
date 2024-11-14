#删除比701插入要复杂很多，因为插入都可以在叶子节点找到位置，但是删除就不是我们能控制的了，所以就可能会出现结构的改变
#分析思路，直接看图，有几种删除的情况呢？
#1.没找到要删除的节点 2.叶子节点左空右空 3.左不空右空 4.左空右不空 5.左不空右不空 按找没找到分大类 前一种 和后四种 
#5有两种处理方法，让右孩子继位或者左孩子继位都可以，选一种即可，我选的是右孩子继位，那么要把左孩子接到右子树最左边的节点上（因为首先右孩子继承了，上方就没有空位了，那么右孩子所在的右子树，里面要找一个比目标节点大点但不能大太多的接上，举个具体例子就懂了）
#这道题实际上不复杂，只是考虑的逻辑要全面，然后根据图把所有情况写出来就可以
class Solution:
    def deleteNode(self, root, key):
        #递归终止条件 找到了即删除 所以把删除逻辑放在终止里面
        if not root:
            return None
        if root.val == key: #找到了要删除的节点
            if not root.left and not root.right:
                return None
            if root.left and not root.right:
                return root.left
            if not root.left and root.right:
                return root.right
            if root.left and root.right:
                cur = root.right
                while cur.left: #别跑到空节点去了 不能是while cur
                    cur = cur.left
                cur.left = root.left
                return root.right
            
        if key < root.val:
            root.left = self.deleteNode( root.left, key)  #每次递归重新开辟一个局部变量root  所以原先的root地址并没有改变 对吗？

        if key > root.val:
            root.right = self.deleteNode( root.right, key) 
            #在类的方法中，调用实例方法比如调用 self.deleteNode 方法时，Python 会自动将 self 作为第一个参数传入，因此您只需提供其余参数，如 root.left 和 key。
#如果您手动提供 self，代码会因为重复传递参数而引发错误。 所以不要写成self.deleteNode(self, root.left, key)

        return root
        


