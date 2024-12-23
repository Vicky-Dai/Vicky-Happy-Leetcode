#然后就是求起点和终点的最短路径长度，这里无向图求最短路，广搜最为合适，广搜只要搜到了终点，那么一定是最短的路径。因为广搜就是以起点中心向四周扩散的搜索。
#本题是一个无向图，需要用标记位，标记着节点是否走过，否则就会死循环！
#使用set来检查字符串是否出现在字符串集合里更快一些

def judge(s1,s2):
    count = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            count += 1
    return count == 1

if __name__ == '__main__':
    n = int(input())
    beginstr, endstr = map(str, input().split())
    if beginstr == endstr:
        print(0)
        exit()
    strlist = []
    for i in range(n):
        strlist.append(input())

    #use bfs
    visit = [False for i in range(n)]
    queue = [[beginstr, 1]]
    while queue:
        str,step = queue.pop(0)
        if judge(str,endstr):
            print(step+1)
            exit()
        for i in range(n):
            if visit[i]==False and judge(strlist[i],str):
                visit[i]=True
                queue.append([strlist[i],step+1])
    print(0)