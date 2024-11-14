class Solution:
   def largestSumAfterKNegations(self, A: list[int], K: int) -> int: 
      A.sort(key=lambda x: abs(x), reverse=True)

      for i in range(len(A)):  # 第二步：执行K次取反操作
            if A[i] < 0 and K > 0:
                A[i] *= -1
                K -= 1

            if K % 2 == 1:  # 第三步：如果K还有剩余次数，将绝对值最小的元素取反  太妙了！！ 如果是偶数转回来还是一样的 如果这里写loop性能就会变差
                A[-1] *= -1

            result = sum(A)  # 第四步：计算数组A的元素和
            return result