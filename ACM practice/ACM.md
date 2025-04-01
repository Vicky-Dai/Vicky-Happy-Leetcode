1. 注意输入输出都是字符串 （特别是输出如果不是字符串就没法直接print还得循环输出）
2. s = input().split() #这里 input是接收一行输入 split是按照空格把输入的字符串切割成数组
3. 如果有多行输入，可以这样处理：
import sys
 
or input in sys.stdin:
    input = input.split()

sys.stdin可以一下子把所有的输入都拿到

（如果第一行和后面的含义不同）也可以这样：
n, m = map(int, input().split()) #这里n可能代表的是行数
    grid = []
    for i in range(n):
        grid.append(list(map(int, input().split())))

4. 处理多行输入但是想一行一行取
sys.stdin.readline() 即使在不同的地方调用，会继续上次读行的地方继续往下读

5. data = sys.stdin.read()  # 一次性读取所有数据
lines = data.strip().splitlines()  # 按行分割数据