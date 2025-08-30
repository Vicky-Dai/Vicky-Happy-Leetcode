class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        freq_min = [float('inf')] * 26
        ans = []

        for word in words:
            freq_arr = [0]*26 #每个word单独计算出现次数
            for char in word:
                freq_arr[ord(char)-ord('a')] += 1
            for i in range(26):
                freq_min[i] = min(freq_min[i], freq_arr[i])

        for i in range(26):
            for _ in range(freq_min[i]):
                ans.append(chr(i + ord('a')))

        return ans
