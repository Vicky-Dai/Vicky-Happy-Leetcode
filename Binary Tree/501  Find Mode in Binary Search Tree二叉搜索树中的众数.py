from TreeNode import TreeNode 

class Solution:
    def __init__(self):
        self.count = 0
        self.maxCount = 0
        self.res = []
        self.pre = None

    def searchBST(self, cur) -> list[int]:
        if not cur:
            return  #递归结束条件
        
        self.searchBST(cur.left) #左  先遍历到最后 左中右的第一个pre一定是从左下角开始的
        if self.pre is None:#第一个节点
            self.count = 1 
        elif self.pre.val == cur.val:#与前一个节点数值相同
            self.count += 1
        else: 
            self.count = 1
        self.pre = cur #更新上一个节点

        #整理众数 #代码技巧 这样就可以通过一次遍历就解决问题
        if self.count == self.maxCount:
            self.result.append(cur.val)

        if self.count > self.maxCount: # 如果计数大于最大值频率
            self.maxCount = self.count #更新最大频率
            self.result = [cur.val] # 很关键的一步，不要忘记清空result，之前result里的元素都失效了

        self.searchBST(cur.right) #右
        return
    
    def findMode(self, root):
        self.count = 0
        self.maxCount = 0
        self.pre = None #记录前一个节点
        self.result = [] 

        self.searchBST(root)
        return self.result

        



