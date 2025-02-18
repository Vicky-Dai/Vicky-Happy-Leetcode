""" 复杂度： O(nklogk)"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)
        
        return list(mp.values())

#defaultdict 的优点：它能自动为每个键初始化一个默认值，避免了手动检查键是否存在的麻烦。