#中序递归法 利用二叉搜索树的性质：二叉搜索树的中序遍历是一个递增序列，那么一定是相邻两个元素比较，出现频率最高的元素输出
#时间复杂度是 O(N)，其中 𝑁是二叉搜索树（BST）中节点的数量。
#用cur遍历一遍
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
            self.count = 1 #与前一个节点数值不同，计数重置为1
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

        

#递归法 利用字典 （像数组那样用字典记录频率）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def searchBST(self, cur, freq_map):
        if cur is None:
            return
        freq_map[cur.val] += 1  # 统计元素频率
        self.searchBST(cur.left, freq_map)
        self.searchBST(cur.right, freq_map)

    def findMode(self, root):
        freq_map = defaultdict(int)  # key:元素，value:出现频率
        result = []
        if root is None:
            return result
        self.searchBST(root, freq_map)
        max_freq = max(freq_map.values())
        for key, freq in freq_map.items():
            if freq == max_freq:
                result.append(key)
        return result

