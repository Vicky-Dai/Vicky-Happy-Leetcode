class Edge:
    def __init__(self, l, r, val):
        self.l = l
        self.r = r
        self.val = val

n = 10001
father = list(range(n))

def init():
    global father
    father = list(range(n))

def find(u):
    if u != father[u]:
        father[u] = find(father[u])
    return father[u]

def join(u, v):
    u = find(u)
    v = find(v)
    if u!= v:
        father[v] = u

def kruskal(v, edges):
    edges.sort(key=lambda edge: edge.val)
    init()
    result_val = 0

    for edge in edges:
        x = find(edge.l)
        y = find(edge.r)
        if x != y:
            result_val += edge.val
            join(x,y)
    return result_val

if __name__ == "__main__":
    import sys
    input = sys.stdin.readdata = input().split() #sys.stdin.read() 会一直读取直到输入结束（如按下 Ctrl + D 或 Ctrl + Z），然后将所有输入合并成一个字符串。
    data = input().split() 

    v = int(data[0])
    e = int(data[1])

    edges = []
    index = 2
    for _ in range(e):
        v1 = int(data[index])
        v2 = int(data[index + 1])
        val = int(data[index + 2])
        edges.append(Edge(v1, v2, val))
        index += 3
    
    result_val = kruskal(v, edges)
    print(result_val)

# 我自己的写法
class UnionFind:
    def __init__(self, v):
        self.father = list(range(v+1))
    
    def find(self, u):
        if u != self.father[u]:
            self.father[u] = self.find(self.father[u])
        return self.father[u]
    
    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            self.father[v] = u

def main():
    v, e = map(int, input().strip().split())
    uf = UnionFind(v)
    edges = []
    for _ in range(e):
        x, y, w = map(int, input().strip().split())
        edges.append((w, x, y))
    edges.sort()
    result = 0
    for edge in edges:
        w, x, y = edge # ！！！！ w放前面为了排序
        if uf.find(x) != uf.find(y):
            uf.join(x, y)
            result += w
    print(result)

if __name__ == "__main__":
    main()

