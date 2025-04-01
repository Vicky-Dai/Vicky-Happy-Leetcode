import sys
for line in sys.stdin:
    print(",".join(sorted(line.strip().split(","))))
    # 注意必须要strip因为原先有换行符