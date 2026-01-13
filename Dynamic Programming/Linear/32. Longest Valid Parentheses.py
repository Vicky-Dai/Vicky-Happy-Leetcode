# stack Time: O(n) Space: O(n)
class Solution:
    def longestValidParenTheses(self, s: str) -> int:
        stack = [-1]
        mx = 0
        for i, p in enumerate(s):
            if p == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    mx = max(mx, i - stack[-1])
        return mx
# dp Time: O(n) Space: O(n)
# dp[i] 表示以第 i 个字符结尾的最长有效括号的长度
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        ans = 0

        for i in range(1, n):
            if s[i] == ')':
                # case 1: "()"
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2

                # case 2: "...))"
                else:
                    prev = i - dp[i-1] - 1
                    if prev >= 0 and s[prev] == '(':
                        dp[i] = dp[i-1] + 2
                        if prev - 1 >= 0: # 如果 prev - 1 >= 0，则需要加上 prev - 1 位置的最长有效括号的长度
                            dp[i] += dp[prev - 1]

                ans = max(ans, dp[i])

        return ans


# Two Pointers Time: O(n) Space: O(1)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = right = 0
        ans = 0

        # Left → Right
        for c in s:
            if c == '(':
                left += 1
            else:
                right += 1

            if left == right:
                ans = max(ans, 2 * right)
            elif right > left:
                left = right = 0

        # Right → Left
        left = right = 0
        for c in reversed(s):
            if c == ')':
                right += 1
            else:
                left += 1

            if left == right:
                ans = max(ans, 2 * left)
            elif left > right:
                left = right = 0

        return ans
