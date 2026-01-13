Array:
-init 
nums = []

-create
nums[0] = a
nums.append(b)
m = nums[:]

-delete
del nums[0]
del nums[1:3]
nums.pop()
nums.pop(0) # delete a specific one
nums[key] = value

-update
nums[0] = 100
nums[1:3] = [,]

-read
nums[key]
nums[-1]
nums.enumerate()
if i in nums
for num in nums
len(nums)
nums.count(3)
nums.index(2)

String:
-init
s = "abc"
-create
s = "abc" + "def"
-delete
s = s[:2] + s[3:]
-update
s = s[:3] + m + s[3:]
-read
s[0]


String
-init
s = ""
s = f"{}"
from_list = "".join(['H', 'e', 'l', 'l', 'o'])

-create
s = ""

-delte
s = [:5] + [7:]
s.replace(" ", "")
s.strip(" ") # 清除空格


-update
s = "" + ""
-read
len(s)
s[i]
s[-1]
s.upper()
s.lower()
s.isalnum()




Hash Table
Dict 
- init
record = {}
from collections import defaultdict
record = defaultdict(int) #tuple list

- create
record[key] = value
record.extend({1:2, 2:3})


- delete
del record[key]
record.pop(key)
record.remove(key)

- update
record[key] = value

- read
for key, value in record.items()
for key in record.keys()
for key in record.value()
record.get(key, default)




set
-init
record = set() # only keep one element once 
-create
record.add(a)
-delete()
record.remove()
-update
-read
if i in record



Queue - Array
- init
queue = []
- create
queue.append()
- delete
queue.popleft()
- update
- read

Priority Queue
-init
import heapq
heap = []
heap.heapify()
top = []
-create
heapq.heappush(top, (a, b))


-delete
heapq.heappop()

-update
heapq.heapreplace(top, c)
-read
smallest = min_heap[0]
largest = -max_heap[0]

n_smallest = heapq.nsmallest(3, min_heap)
n_largest = heapq.nlargest(3, min_heap)


