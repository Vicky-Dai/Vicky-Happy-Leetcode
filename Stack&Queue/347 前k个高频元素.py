import heapq
class Solution:
    def topKFrequent(self, nums: list[int], k:int) -> list[int]:
        #要统计元素出现频率
        map_ = {} #key 元素  value 出现频率
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1 #map_.get(nums[i], 0) 是字典 map_ 的 get 方法。它尝试从字典中获取 nums[i] 这个键对应的值。如果 nums[i] 这个键不存在于字典中，它会返回默认值 0
    
        #对频率排序
        #定义一个小顶堆，大小为k
        pri_que =[]

        #用固定大小为k的小顶堆，扫描所有频率的数值
        for key, freq in map_.items(): #dict.item()返回所有对象，包含了所有键值对
            heapq.heappush(pri_que, (freq, key))  #向其中push数据
            if len(pri_que) > k: #控制窗口
                heapq.heappop(pri_que)

        #找出前k个高频元素，因为小顶堆先弹出的是最小的，所以倒序来输出到数组
        result = [0]*k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1] #[1]：访问弹出元素元组的第二个值。假设堆中的元素是 (freq, key) 形式的元组，heapq.heappop(pri_que) 会返回 (freq, key)，那么 [1] 就是 key。
        return result  #python中键值对通常用元组的形式表示
