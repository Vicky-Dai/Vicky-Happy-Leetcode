class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size + 1)) #将 range 生成的序列转换为一个列表。这样，self.parent 将是一个从 0 到 size 的整数列表。
        # 初始化每个节点的父节点为自己

    def find(self, u): #用于找到根节点
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u]) #路径压缩，把到根节点比较多的节点直接挂到根节点上
        return self.parent[u]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v) #找到需要联合的两个节点各自的根节点，如果不是相同的也就是不是同一个集合的，把后者的根节点指向前者的根节点
        if root_u != root_v:
            self.parent[root_v] = root_u

    def is_same(self, u, v):
        return self.find(u) == self.find(v)
    
def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    index = 0
    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1

    uf = UnionFind(n) #初始化并查集

    for _ in range(m):
        s = int(data[index])
        index += 1
        t = int(data[index])
        index += 1
        uf.union(s, t) #根据输入不断地联合两个节点

    source = int(data[index]) #求的来源
    index += 1
    destination = int(data[index]) #求的终点

    if uf.is_same(source, destination):
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()


""" 
main直接用函数写：
1. 类和实例方法的调用
在 Python 里，类的方法（如 def is_same(self, u, v):）必须通过类的实例（对象）来调用，self 代表当前对象。
如果你在类外部直接写 return self.find(u) == self.find(v)，没有 self 这个对象，代码会报错。
2. 主流程应该用函数，不要用类
main 通常是程序的主入口，应该写成普通函数（def main():），而不是类（class main:）。
只有需要封装数据和行为时才用类。
3. return 和 print 的区别
return 是函数返回值，只有调用者能接收到。
print 是直接输出到标准输出，OJ/ACM模式下评测系统只能看到 print 的内容。
4. 实例化对象后调用方法
你应该先创建对象（如 uf = UnionFind(n)），然后用 uf.is_same(u, v) 这样的方法调用。 """