#原始题目没有给定数组元素大小限制，因此如果用数组这种连续的存储结构，需要考虑数组哈希表越界的问题，以及空间的浪费。因此可以使用set
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # 使用哈希表存储一个数组中的所有元素
        table = {}
        for num in nums1:
            table[num] = table.get(num, 0) + 1
            #table.get(key, default)是dict的方法，用于获取key对应的值，如果key不存在，则赋予后面default的默认值
        
        # 使用集合存储结果
        res = set()
        for num in nums2: #遍历第二个数组
            if num in table: #检查在第一个数组中是否出现过
                res.add(num)  #如果出现过就添加到最终结果中
                del table[num] #删掉是为了保证不要重复出现
        
        return list(res)