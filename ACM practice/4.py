import sys
while True:
    s = list(map(int,sys.stdin.readline().strip().split()))
     
    if s[0] == 0:
        break
    else:
        print(sum(s[1:]))