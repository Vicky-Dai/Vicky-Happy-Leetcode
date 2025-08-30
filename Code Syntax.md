1. 哈希表
是的，Python 的 dict（哈希表）确实有 pop() 方法，用于删除字典中的指定键，并返回该键对应的值。
字典的键必须是可哈希的，而列表（list）是不可哈希的，这意味着列表不能作为字典的键。因此，如果你想用一个可变序列（比如 matrix 这样的列表）作为字典的键，必须先将其转换为不可变的类型，而 元组（tuple）是不可变的，所以元组可以作为字典的键。

在代码中：
self.cache.pop(removed.key)

2. 字符串
s.count(‘0’) 计算有多少个0
.join()用于将一个可迭代对象（如列表、元组等）中的元素连接成一个新的字符串。
separator.join(iterable)
separator：作为连接符的字符串。
iterable：一个可迭代的对象，如列表、元组等。

3. 列表
sum(iterable, start) 例如 sum(s[1:]) 可以把可迭代对象进行求和，start可不填，默认是0
map(function, iterable, ...)
map() 是 Python 的一个内置函数，用于 对可迭代对象中的每个元素应用指定的函数，并返回一个 map 对象（可迭代）。

# 删除指定索引位置的元素
del my_list[2]  # 删除索引为 2 的元素（值为 3）
print(my_list)   # 输出: [1, 2, 4, 5]

# 删除整个列表
del my_list

# 删除第一个出现的 3
my_list.remove(3)

# 删除并返回指定索引位置的元素
item_at_index_1 = my_list.pop(1)

# 切片删除：删除从索引 1 到索引 3 的元素（不包括索引 3）
my_list[1:3] = []

1. 增（Create）—— 添加元素
这些方法用于向列表中添加元素，相当于“往购物车里放东西”。

方法	作用	示例
append(x)	在列表末尾添加元素 x	lst.append(5)
insert(i, x)	在索引 i 处插入元素 x	lst.insert(2, 10)
extend(iterable)	将 iterable（如列表、元组）中的所有元素添加到列表末尾	lst.extend([4, 5, 6])
+（拼接）	合并两个列表	new_list = lst1 + lst2
*（重复）	复制列表 n 次	lst * 3
🔹 比喻：就像往购物车里放新商品，直接放、插入到某个位置，或者合并多个购物车的商品。

2. 删（Delete）—— 删除元素
这些方法用于从列表中移除元素，相当于“从购物车里拿走东西”。

方法	作用	示例
remove(x)	删除列表中第一个匹配的元素 x，如果不存在则报错	lst.remove(3)
pop(i)	删除并返回索引 i 处的元素（默认最后一个）	x = lst.pop(2)
del lst[i]	通过索引 i 删除元素	del lst[1]
del lst[start:end]	通过切片删除多个元素	del lst[1:3]
clear()	删除所有元素，使列表变空	lst.clear()
🔹 比喻：像是购物时从购物车里移除某个商品、拿走最后放进去的商品，或者把购物车整个清空。

3. 改（Update）—— 修改元素
这些方法用于更改列表中的元素，相当于“更换购物车里的某些商品”。

方法	作用	示例
lst[i] = x	修改索引 i 处的元素为 x	lst[2] = 99
lst[start:end] = new_list	通过切片修改多个元素	lst[1:3] = [7, 8]
reverse()	反转列表元素的顺序	lst.reverse()
sort()	对列表进行排序（默认升序）	lst.sort()
sort(reverse=True)	对列表降序排序	lst.sort(reverse=True)
🔹 比喻：像是换掉购物车里的某个商品、调整购物车里的商品顺序。

4. 查（Read）—— 访问元素
这些方法用于查询或访问列表中的元素，相当于“查看购物车里的东西”。

方法	作用	示例
lst[i]	访问索引 i 处的元素	print(lst[1])
lst[-1]	访问最后一个元素	print(lst[-1])
len(lst)	获取列表长度（元素个数）	print(len(lst))
lst[start:end]	获取列表的子列表（切片）	sub_lst = lst[1:3]
count(x)	统计元素 x 在列表中出现的次数	lst.count(2)
index(x)	获取元素 x 在列表中的第一个索引	lst.index(4)
in 关键字	判断元素是否在列表中	if 3 in lst:
for 循环	遍历列表	for item in lst: print(item)
🔹 比喻：像是在购物车里查看某个商品、数一数总共有多少件商品，或者查找某个商品的位置。

5. 其他高级操作
这些方法提供一些特殊的列表处理方式。

方法	作用	示例
copy()	复制列表（浅拷贝）	new_lst = lst.copy()
sorted(lst)	返回排序后的新列表（不会改变原列表）	sorted_lst = sorted(lst)
lst[start:end:step]	通过步长 step 获取子列表	lst[::2]（隔一个取一个）
🔹 比喻：像是复制购物车里的商品、对购物车里的商品重新排序等。

最终总结
增（Create）：append()、insert()、extend()、+、*
删（Delete）：remove()、pop()、del、clear()
改（Update）：直接赋值、切片赋值、reverse()、sort()
查（Read）：索引访问、len()、切片、count()、index()、in、for 遍历
🔹 比喻整体记忆法

增：往购物车里加商品
删：从购物车里拿走商品
改：换掉购物车里的商品
查：查看购物车里的商品、数一数、找位置



# 使用 chr() 将 Unicode 编码转为字符
char = chr(97)  # 97 是字母 'a' 的 Unicode 编码
print(char)  # 输出: a

# 使用 ord() 获取字符的 Unicode 编码
unicode_code = ord('a')  # 获取字符 'a' 的 Unicode 编码
print(unicode_code)  # 输出: 97


4. 字符串
char.isdigit()是否只包含数字
char.isalpha()


# 优先队列
heapq.heappop() 是从下标 0（也就是堆顶）弹出元素的，不是从右边！

方法名	作用说明	示例代码片段	备注
heapq.heapify(iterable)	将列表原地转换成最小堆	heapq.heapify(data)	原地修改，不返回新列表
heapq.heappush(heap, item)	向堆中添加元素，保持堆结构	heapq.heappush(data, 3)	时间复杂度 O(log n)
heapq.heappop(heap)	弹出并返回最小元素	min_val = heapq.heappop(data)	堆必须非空
heapq.heappushpop(heap, item)	先推入再弹出最小元素，效率高于先 push 后 pop	val = heapq.heappushpop(data, item)	时间复杂度 O(log n)
heapq.heapreplace(heap, item)	先弹出最小元素再推入新值	val = heapq.heapreplace(data, item)	与上一个方法顺序相反
heapq.nlargest(n, iterable)	返回前 n 大的元素（按降序）	heapq.nlargest(3, nums)	非堆结构也可使用
heapq.nsmallest(n, iterable)	返回前 n 小的元素（按升序）	heapq.nsmallest(2, nums)	可用于快速找极小值
