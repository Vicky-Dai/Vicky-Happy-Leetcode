#子序列是指一个序列中的某些元素按照原序列的相对顺序排列而成的新序列。所以本题不可以重新排序
#本题也是子集类问题，要搜索所有的节点，只是对所有的节点要加限制条件，所以也不需要写终止条件
#关于终止条件的思考：终止条件和循环条件是两回事，求所有节点的是对节点循环到所有能循环的都加进去，所以循环和终止条件就重合了；
# 但是结果在叶子节点上的不是这样，因为循环到的不一定是我想要的，终止条件和循环条件是不一致的，所以一定要加终止条件
#本题要树层去重，还有题目要求的去重（至少两个元素，递增）

class Solution:
    def findSubsequences(self, nums):
        path = []
        result = []
        self.backtracking(nums, path, result, 0)
        return result
    
    def backtracking(self, nums, path, result, start_index):
        #本题直接收集元素，不需要终止
        if len(path) > 1:
            result.append(path[:])  # 注意要使用切片将当前路径的副本加入结果集
            #path 是一个可变的对象（列表）。如果你直接将 path 添加到 result 中，而不使用切片拷贝，当 path 发生变化时，result 中的值也会随之改变。
            # 注意这里不要加return，要取树上的节点
        
        usedt = set() #注意set的位置，本题树层去重，树枝不去重。在for和递归结合体里面到底哪里是层哪里是枝？for循环带领的当前递归：栈临时元素就是一层（横着点数，注意只在一个子树里），也就是上一个递归下面的几个结果
        #而树枝是竖着一直递归往下走，在这里，set要放在for之前递归之内，保证每次递归都重新刷新一遍set
        for i in range(start_index, len(nums)):
            if (path and nums[i] < path[-1]) or nums[i] in usedt: #注意这里加括号 #加不加 i > start_index 都能通过，因为set每次递归都会更新
                continue
            usedt.add(nums[i])
            path.append(nums[i])
            self.backtracking(nums, path, result, i+1)
            path.pop()

