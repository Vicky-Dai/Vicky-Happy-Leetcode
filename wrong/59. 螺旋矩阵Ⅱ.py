class Solution:
    def juanjuan(self, n:int )->list[int][int]:
        startx, starty, count, i = 0, 0, 1, 1 #起始点位置不要动 否则没有参照物

        loop = n //2
        offset = 1
        nums = list[int][int]

        #左闭右开原则

        while i<=loop:
            for m in range(startx, n-offset-1):  #这里容易出错，首先范围必须是能活动的，否者如果有内圈如何自动更新，且必须是外层更新，这是根据逻辑来的。其次计数器/循环变量i需要
                nums[startx][starty] = count
                starty += 1
                count += 1
        
            for m in range(starty, n-offset-1): #从上到下
                nums[startx][starty] = count
                startx += 1
                count += 1
                
            for m in range(startx, offset, -1):  #（大，小，负步长） 当年你需要从高到低进行的时候 范围前大后小是合法的
                nums[startx][starty] = count
                starty -= 1
                count += 1

            for m in range(starty, n-offset, -1):
                nums[startx][starty] = count
                startx -= 1
                coun += 1

            i += 1 
            startx += 1
            starty += 1   
        

            
                
