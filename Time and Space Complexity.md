1. 计算方法


2. 其他总结
（1）logn通常就是来自于每次范围递减一半

O(log n) 时间复杂度主要来源于**分治思想**和**每次操作都能将问题规模减半**的算法。

## 核心原理

当算法每次执行都能将数据量减少一半时，就会产生 O(log n) 复杂度：

```

n → n/2 → n/4 → n/8 → ... → 1

```

需要多少步才能从 n 减到 1？答案是 log₂(n) 步。

## 典型例子

**1. 二分查找**

```python

python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1# 排除左半部分
        else:
            right = mid - 1# 排除右半部分
    return -1

# 每次循环都排除一半元素# 1000个元素 → 500 → 250 → 125 → ... → 1# 大约需要 log₂(1000) ≈ 10 次操作

```

**2. 平衡二叉树操作**

```python

python
# 在平衡二叉树中查找# 树高为 log n，最多需要从根到叶子遍历一次
def search_bst(root, target):
    while root:
        if root.val == target:
            return root
        elif target < root.val:
            root = root.left# 排除右子树
        else:
            root = root.right# 排除左子树
    return None

```

**3. 分治算法的递归层数**

```python

python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])# 递归处理一半
    right = merge_sort(arr[mid:])# 递归处理另一半

    return merge(left, right)

# 递归深度 = log n 层# 但每层需要 O(n) 时间合并，所以总体是 O(n log n)

```

## 数学推导

如果每次操作将规模从 n 变为 n/2：

- 第1步：n
- 第2步：n/2
- 第3步：n/4
- ...
- 第k步：n/2^k = 1

解这个方程：2^k = n，所以 k = log₂(n)