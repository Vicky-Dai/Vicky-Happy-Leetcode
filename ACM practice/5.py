import sys

t = int(sys.stdin.readline().strip())

for _ in range(t):
    s = list(map(int,sys.stdin.readline().strip().split()))
    print(sum(s[1:]))
             