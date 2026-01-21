from sortedcontainers import SortedDict
from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.m = defaultdict(SortedDict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.m[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.m[key]
        index = timestamps.bisect_right(timestamp) - 1 # 找到最大index 实现index <= timestamp
        if index >= 0:
            closest_time = timestamps.iloc[index]
            return timestamps[closest_time]
        else:
            return ""
        
""" bisect_left → 第一个 ≥ x 的位置
bisect_right → 第一个 > x 的位置 """

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)