import sys
 
for line in sys.stdin:
    print(' '.join(sorted(line.split())))