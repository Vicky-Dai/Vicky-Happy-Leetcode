import sys
for line in sys.stdin:
    s = list(map(int, line.strip().split()))
    print(sum(s))

# 如果提交为0怀疑一下自己是不是理解错了题目