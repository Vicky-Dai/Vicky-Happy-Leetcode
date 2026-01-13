# stack
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # when meet the operator pop the two operands in the stack, calculate
        import operator
        mapp = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b)
        }
        stack = []
        res = 0
        for t in tokens:
            if t in mapp:
                prev = stack.pop() #2
                ne = stack.pop() #1
                operator = mapp[t] # +
                res = operator(ne, prev) #
                stack.append(res) #3
            else:
                stack.append(int(t)) # 1, 2
        return stack[0]

# recursion
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            token = tokens.pop()
            if token not in "+-*/":
                return int(token)

            right = dfs()
            left = dfs()

            if token == '+':
                return left + right
            elif token == '-':
                return left - right
            elif token == '*':
                return left * right
            elif token == '/':
                return int(left / right)

        return dfs()