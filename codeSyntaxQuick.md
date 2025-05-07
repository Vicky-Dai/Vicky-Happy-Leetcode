📌 1. 列表（List）
列表是 Python 最常用的数据结构之一，支持增删改查等多种操作。
一种简洁的构造方式：[1] + [0] * n 

操作	方法	作用	示例
增（Create）	append(x)	追加元素到末尾	lst.append(5)
insert(i, x)	在索引 i 处插入元素 x	lst.insert(2, 10)          !!!!!
extend(iterable)	合并另一个列表	lst.extend([4, 5, 6])
+	拼接列表	new_lst = lst1 + lst2                               !!!!!!
*	复制列表	lst * 3
删（Delete）	remove(x)	删除第一个匹配的 x	lst.remove(3)
pop(i)	删除并返回索引 i 处的元素	x = lst.pop(2)
del lst[i]	删除索引 i 处的元素	del lst[1]
clear()	清空列表	lst.clear()
改（Update）	lst[i] = x	修改索引 i 处的元素	lst[2] = 99
reverse()	反转列表	lst.reverse()                       !!!
sort()	排序列表	lst.sort()
查（Read）	lst[i]	访问索引 i 处的元素	print(lst[1])
len(lst)	获取列表长度	print(len(lst))
count(x)	统计 x 在列表中的出现次数	lst.count(2)
index(x)	获取 x 的索引	lst.index(4)
for 遍历	遍历列表	for item in lst: print(item)

2. 字符串是
 Python 中的不可变序列，常用于文本处理。常用操作包括切片、查找、替换、格式化等。
 空字符串	'' / str()	表示一个空的字符串
操作	方法 / 表达式	作用	示例
增（拼接）	+	拼接两个字符串	'Hello, ' + 'world' → 'Hello, world'
*	重复字符串	'ha' * 3 → 'hahaha'
删（生成新串）	replace(old, new)	替换字符串中所有的 old 为 new	'apple'.replace('p', '') → 'ale'
改（生成新串）	upper() / lower()	转为大写 / 小写	'Hi'.lower() → 'hi'
strip() / lstrip() / rstrip()	去除首尾空白符	' hi '.strip() → 'hi'
replace(old, new)	替换字符	'foo'.replace('f', 'b') → 'boo'
查（查询）	in	判断子串是否存在	'a' in 'cat' → True
find(sub) / index(sub)	查找子串索引	'hello'.find('e') → 1
count(sub)	统计子串出现次数	'banana'.count('a') → 3
startswith(s) / endswith(s)	判断开头/结尾	'hello'.startswith('he') → True
切片 / 访问	s[i]	访问索引 i 处字符	'abc'[1] → 'b'
s[i:j]	获取子串（左闭右开）	'hello'[1:4] → 'ell'
len(s)	获取字符串长度	len('abc') → 3
遍历	for c in s	遍历字符串中的每个字符	for c in 'hi': print(c)
格式化	f"..."	f-string 格式化	f"Hi {name}" → 'Hi Tom'
"{} {}".format(a, b)	使用 format 函数	"{} and {}".format('A', 'B')
判断类型	isalpha() / isdigit()	是否全字母 / 全数字	'abc'.isalpha() → True
isalnum() / isspace()	是否字母或数字 / 空格	'abc123'.isalnum() → True


📌 2. 元组（Tuple）
元组是不可变的列表，因此只支持 查找，但不支持 修改、删除、添加。

操作	方法	作用	示例
增（Create）	(a, b, c)	创建元组	tup = (1, 2, 3)
+	拼接元组	new_tup = tup1 + tup2
*	复制元组	tup * 3
查（Read）	tup[i]	访问索引 i 处的元素	print(tup[1])
len(tup)	获取元组长度	print(len(tup))
count(x)	统计 x 的出现次数	tup.count(2)
index(x)	获取 x 的索引	tup.index(4)
for 遍历	遍历元组	for item in tup: print(item)
解包  从一个元组或列表把里面的元素解出来   pair = (3, 5)  a, b = pair  # a=3, b=5
🔹 比喻：元组就像一个“锁定的购物车”，你可以查看，但不能改动。

📌 3. 集合（Set）
集合是一种无序、不可重复的数据结构，适用于去重和集合运算。

操作	方法	作用	示例
增（Create）	add(x)	添加元素 x	s.add(5)
update(iterable)	批量添加元素	s.update([1, 2, 3])
删（Delete）	remove(x)	删除 x，若不存在报错	s.remove(3)
discard(x)	删除 x，不存在不会报错	s.discard(4)
pop()	随机删除一个元素	x = s.pop()
clear()	清空集合	s.clear()
改（Update）	❌	集合是无序的，不支持索引修改	❌
查（Read）	in 关键字	判断元素是否在集合中	if 3 in s:
len(s)	获取集合大小	print(len(s))
for 遍历	遍历集合	for item in s: print(item)
🔹 比喻：集合像是一个“去重后的购物篮”，不支持索引访问，但可以判断是否存在某个商品。

📌 4. 字典（Dictionary）
字典是键值对存储结构，支持 键值操作、查询和修改。
初始化：
普通dict  mapper = dict() 或 mapper = {}
defaultdict  mapper = collections.defaultdict(int) #!!!! 注意初始化  

操作	方法	作用	示例
增（Create）	dict[key] = value	添加键值对	d['name'] = 'Alice'
update(dict2)	合并另一个字典	d.update({'age': 25})
删（Delete）	pop(key)	删除并返回 key 对应的值	name = d.pop('name')
del d[key]	删除 key	del d['age']
clear()	清空字典	d.clear()
改（Update）	d[key] = new_value	修改 key 对应的值	d['name'] = 'Bob'
查（Read）	d[key]	获取 key 对应的值	print(d['name'])
get(key, default)	获取 key 值，不存在则返回 default	d.get('age', 0) 获取age这个key对应的值，如果没有则为0
keys()	获取所有键	d.keys()
values()	获取所有值	d.values()
items()	获取所有键值对	d.items()
for 遍历	遍历字典	for k, v in d.items(): print(k, v)
🔹 比喻：字典像是一个“购物清单”，你可以根据商品名称（键）查找价格（值），也可以修改或删除商品。

注意：
mapp = {"a": 2, "b": 3}
v = mapp.values() 此时的 v 不是一个列表，而是一个 视图对象，准确说是一个 dict_values 对象。
打印出来是这样的：dict_values([2, 3]) 这个对象是 动态的、可迭代的，但它不是列表，也不是索引序列  如果你想索引访问，就要转成列表：
v = list(mapp.values())


📌 总结对比
数据结构	是否有序	是否可变	适用场景
列表（list）	✅ 是	✅ 可变	适合存储有序数据，可增删改查
元组（tuple）	✅ 是	❌ 不可变	适合存储不可修改的数据
集合（set）	❌ 无序	✅ 可变	适合去重和集合运算
字典（dict）	❌ 无序	✅ 可变	适合键值存储、快速查找


all(...)：这个是 Python 的内置函数，用来判断 所有条件都为真。