import sys
while True:
    nums = list(map(int, sys.stdin.readline().strip().split()))
    if not nums:
        break
    print(sum(nums[1:]))