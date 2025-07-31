father = list()

def find(u):
    if u == father[u]:
        return u
    else:
        father[u] = find(father[u])
        
def is_same(u, v):
    u = find(u)
    v = find(v)
    return u == v

def join(u, v):
    u = find(u)
    v = find(v)
    if u != v:
        father[u] = v

if __name__ == "__main__":
    n = int(input())
    for i in range(n+1):
        father.append(i) #初始化并查集，让每个链表的father都是自己
    result = None
    for i in range(n):
        s, t = map(int, input().split())
        if is_same(s,t):
            result = str(s) + '' + str(t) # 这个写法很方便
        else:
            join(s, t)

    print(result)

# 我自己写的
class UnionFind:
    def __init__(self, n):
        self.father = list(range(n+1)) # ！！！！！注意书写细节

    def find(self, u):
        if u == self.father[u]:
            return u 
        else:
            self.father[u] = self.find(self.father[u]) # ！！！！！注意书写细节
            return self.father[u]
    
    def is_same(self, u, v):
        u = self.find(u) # ！！！！！注意书写细节
        v = self.find(v)
        return u == v
    
    def join(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            self.father[u] = v
    
def main():
    n = int(input())
    uf = UnionFind(n)
    res = None
    for i in range(n):
        s, t = map(int, input().split())
        if uf.is_same(s, t):
            res = str(s) + ' ' + str(t) 
        else:
            uf.join(s, t)
    print(res)

if __name__ == "__main__":
    main()
