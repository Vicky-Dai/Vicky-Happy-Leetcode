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
            result = str(s) + '' + str(t)
        else:
            join(s, t)

    print(result)