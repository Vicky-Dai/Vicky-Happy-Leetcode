import sys

n = int(sys.stdin.readline().strip())
str = sys.stdin.readline().strip().split()
str.sort()
print(' '.join(str))
    