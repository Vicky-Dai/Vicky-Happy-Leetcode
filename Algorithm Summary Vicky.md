1. 所有算法的基本思路
先人脑以一个逻辑思路把过程大致逻辑出来
用计算机语言去描述和遍历

2. 数据结构模式识别
key-value想到哈希 o1时间用key找到值
出入顺序：栈 队列 表

3. 时间复杂度
“每个数字都要访问/处理一遍，一共有 n 个数字，所以时间复杂度是 O(n)”
结构	时间复杂度
单层循环	O(N)
两层循环	O(N²)
i *= 2 循环	O(logN)
递归分治	通常是 O(NlogN) 或 O(logN)

4. 说句实在话，什么kmp，不就是找已遍历过的部分是否有要查找的元素，什么前缀后缀，就是已遍历过的部分的前面是否等于后面，什么next数组，就是统计相等元素的数量

5. dp和图的联系：dp就是图加上memory
 DP 问题可以转化为图问题
在很多 DP 问题中：
每一个“状态”可以看作是一个“图的节点”。
每一个“状态转移”可以看作是“从一个节点到另一个节点的有向边”。
比如在斐波那契数列中：
状态 f(n) 依赖于 f(n-1) 和 f(n-2)。

可以视为一个有向图，其中 f(n-1) -> f(n) 和 f(n-2) -> f(n) 是边。
如果你把 DP 的状态转移过程看作是在图中遍历路径，那么：
图：描述了所有可能的状态与转移方式。
Memory（记忆化）：保存中间结果，防止重复走相同的路径（即避免重复计算）。
所以，这句话的含义可以理解为：
DP 就是在图上做遍历（通常是 DAG 上），然后加上记忆化（缓存子问题解）来优化搜索的过程。

 例子说明：爬楼梯问题
假设你每次可以爬 1 步或 2 步，求爬到第 n 层的方案数。
每个楼梯 i 是一个状态（节点）。
可以从 i-1 或 i-2 走到 i（图中的边）。
如果你用 DFS + 记忆化（memory），就是在图中查找所有路径，并避免重复计算 —— 这就是 DP。

6. binary search， 如果不是从中间切分逐渐找到目标也算bs

7. 什么情况用什么数据结构
🧠 Data Structures Overview: Features & Use Cases
📦 1. Array / List
Type: Ordered, indexable collection

Key Features:

Fast random access: O(1) by index

Fixed or dynamic length (Python list is dynamic)

Common Use Cases:

Store ordered data

Sliding window problems

Prefix sum arrays

Two-pointer techniques

🔁 2. Stack
Type: LIFO (Last In, First Out)

Operations: push, pop, peek → all O(1)

Common Use Cases:

Valid parentheses

Undo operations

Expression evaluation (e.g., RPN)

Monotonic stack (for "next greater element" types)

🔄 3. Queue / Deque
Type: FIFO (First In, First Out) or double-ended

Queue: enqueue, dequeue → O(1) with collections.deque

Deque: Insert/remove from both ends

Common Use Cases:

BFS (Breadth-First Search)

Sliding window maximum

Topological sort (Kahn's algorithm)

Scheduling problems

🧱 4. Hash Map / Dictionary (dict)
Type: Key-value store

Time Complexity: O(1) average for get, put

Common Use Cases:

Frequency counting

Caching (e.g., LRU)

Storing state or visited nodes

Two-sum problems

🔄 5. Defaultdict / Counter
Type: Smart dictionary

Defaultdict: Avoids key errors, auto-initializes

Counter: For counting elements

Common Use Cases:

Grouping (e.g., anagrams)

Frequency problems

Multisets

🔠 6. Set
Type: Unordered collection of unique elements

Time Complexity: O(1) for add, remove, and search

Common Use Cases:

Duplicate detection

Membership checks

Two-pointer or sliding window optimizations

Fast lookups

🌳 7. Tree / Binary Tree
Type: Hierarchical data

Variants: BST (ordered), AVL/Red-Black (balanced), Trie

Common Use Cases:

Hierarchical relationships (e.g., filesystems)

DFS / recursion problems

Parsing expressions

Trie: prefix search, autocomplete

🔢 8. Heap / Priority Queue
Type: Binary heap (min-heap or max-heap)

Time Complexity: O(log n) for insert and pop

Common Use Cases:

Top-k problems

Dijkstra's algorithm

Task scheduling

Median maintenance

🧭 9. Graph (Adjacency List / Matrix)
Type: Nodes + edges (can be directed/undirected)

Representations:

Adjacency list: space efficient (defaultdict(list))

Matrix: quick edge lookup

Common Use Cases:

Pathfinding (BFS, DFS, Dijkstra)

Cycle detection

Topological sort

Union-Find: connected components

⚙ 10. Union-Find / Disjoint Set
Type: Set manager for merging and finding groups

Time Complexity: Nearly O(1) with path compression

Common Use Cases:

Cycle detection in graphs

Kruskal’s MST

Connected components

Network connectivity

💬 Bonus: When to Think of a Data Structure?
Problem Pattern	Try Using
"I need fast lookups"	set, dict
"I need to maintain order"	list, deque, heap
"I need to process in order added"	queue, deque (BFS)
"I need to undo / reverse quickly"	stack
"I need top/bottom k values"	heap, Counter.most_common()
"I need to manage dependencies"	graph + topological sort
"I need groupings"	defaultdict(list) or Union-Find
"I need to search by prefix"	Trie

