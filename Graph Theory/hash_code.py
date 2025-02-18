#Python中dict和set的创建、添加、删除语法总结
#dict 创建
d = {}
d = dict()
#带初始值的创建
d = {'a': 1, 'b': 2}
d = dict(a=1, b=2)
d = dict([('a', 1), ('b', 2)])
#添加元素
d['c'] = 3  # 如果'c'存在则更新，不存在则添加
d.update({'d': 4})  # 批量更新
d.update(e=5, f=6)  # 直接添加


#set 创建
s = set()
#set带初始值创建
s = {1, 2, 3}
s = set([1, 2, 3])
#添加
s.add(4)
s.update([5, 6, 7]) #批量添加
#删除
s.remove(3)  # 元素不存在会报错
s.discard(3)  # 元素不存在不会报错

 
