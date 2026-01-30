#把每辆车“单独到终点需要的时间”算出来，
#从离终点最近的车开始，只要后面的车能更早到终点，它一定会追上前面的车，于是合并成一个车队。
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []
        for p, s in pair:  # Reverse Sorted Order
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)