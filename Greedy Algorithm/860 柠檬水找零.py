#先分析一下不同价格的具体情况 10和5都是固定的
#贪心，只有20需要分析，贪的是局部先用10和5找零

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five = 0
        ten = 0
        twenty = 0
        
        for bill in bills:
            if bill == 5:
                five += 1

            if bill == 10:
                if five < 1:
                    return False
                five -= 1
                ten += 1

            if bill == 20:
                if five > 0 and ten >0:
                    five -= 1
                    ten -= 1
                    twenty += 1
                elif five >= 3:
                    five -= 3
                    twenty += 1
                else: return False

        return True

                
                
