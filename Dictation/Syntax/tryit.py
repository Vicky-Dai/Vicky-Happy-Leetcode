numbers = [1,2,3,4,5]
s = set(numbers)
s |= {6,7,8,9,10}
print(s)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
union = set1 | set2                # {1, 2, 3, 4, 5, 6}
intersection = set1 & set2         # {3, 4}
difference = set1 - set2           # {1, 2}
symmetric_diff = set1 ^ set2       # {1, 2, 5, 6}
print(union)
print(intersection)
print(difference)
print(symmetric_diff)
