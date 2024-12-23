def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    #读取 n 和 m
    n = int(data[0])
    m = int(data[1])

    #初始化grid
    grid = []
    index = 2
    for i in range(n):
        grid.append([int(data[index +j]) for j in range(m)])
        index += m

    sum_land = 0 #陆地数量
    cover = 0 #相邻shuliang

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                sum_land += 1
                #统计上边相邻陆地
                if i - 1 >= 0 and grid[i-1][j] == 1:
                    cover += 1
                #统计左边相邻陆地
                if j - 1 >= 0 and grid[i][j-1] == 1:
                    cover += 1
                #不统计下边和右边，避免重复计算
    result = sum_land * 4 - cover * 2
    print(result)

if __name__ == "__main__":
    main()


""" 假设你的输入是这样一个 3x3 的数字矩阵：

复制代码
1 2 3
4 5 6
7 8 9
代码流程：
sys.stdin.read() 会读取整个输入内容：


"1 2 3\n4 5 6\n7 8 9\n"
split() 会按空白字符分割这个字符串，得到一个一维的列表：
['1', '2', '3', '4', '5', '6', '7', '8', '9'] """