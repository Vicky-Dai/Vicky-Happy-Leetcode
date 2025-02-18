stack = []

# 入栈
stack.append(1)
stack.append(2)
stack.append(3)

print(stack)  # 输出: [1, 2, 3]

# 出栈
top = stack.pop()
print(top)    # 输出: 3
print(stack)  # 输出: [1, 2]


queue = []

# 入队
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # 输出: [1, 2, 3]

# 出队
front = queue.pop(0) #注意这里，专门写了pop（0）所以才把前面的pop出来
print(front)  # 输出: 1
print(queue)  # 输出: [2, 3]


m = []

# 入栈
m.append(1)
m.append(2)
m.append(3)

print(m)  # 输出: [1, 2, 3]

# 出栈
top = m.pop()
print(top)    # 输出: 3
print(m)  # 输出: [1, 2]

print("====================================")
from collections import deque

# 双端队列测试初始化队列
queue = deque()

# 入队
queue.append(1)
queue.append(2)
queue.append(3)

print(queue)  # 输出: deque([1, 2, 3])

# 出队
front = queue.popleft()  # 注意这里使用 popleft()，它是从队列的前端移除元素
print(front)  # 输出: 1
print(queue)  # 输出: deque([2, 3])

# 查看队列的第一个元素（但不删除）
if queue:
    front_element = queue[0]
    print(f"Front element: {front_element}")  # 输出: 2

# 检查队列是否为空
print(f"Is the queue empty? {len(queue) == 0}")  # 输出: False

# 获取队列的长度
print(f"Queue length: {len(queue)}")  # 输出: 2


# 在 Python 中并没有专门的、单独的栈和队列数据结构，而是通过 list 和 collections.deque 这两个基础数据结构来实现栈和队列的功能。