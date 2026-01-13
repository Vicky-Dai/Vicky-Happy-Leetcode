
class Solution:
    def expand(self, s: str):
        groups = []
        i = 0
        while i < len(s):
            if s[i] == '{':
                j = i
                while s[j] != '}':
                    j += 1
                options = s[i+1:j].split(',')
                groups.append(sorted(options))
                i = j + 1
            else:
                groups.append([s[i]])
                i += 1
            """ imporove
 else:
    j = i
    while j < len(s) and s[j].isalpha():
        j += 1
    groups.append([s[i:j]])
    i = j """

        res = []
        def dfs(index, path):
            if index == len(groups):
                res.append("".join(path))
                return
            for ch in groups[index]:
                dfs(index + 1, path + [ch])

        dfs(0, [])
        return res

""" 🧩 你目前的思路（其实是对的）

“先把大括号拆出来，然后递归生成，再和大括号外的部分 join。”

对！这其实正是 LeetCode 官方推荐解法的核心逻辑。
但为什么你觉得“实现起来很麻烦”？
原因一般有两个：

括号嵌套、字符串扫描、递归这三件事混在一起了，脑子要同时考虑三层逻辑；

没有先把字符串“分组”，直接在原字符串上递归会非常乱。 """