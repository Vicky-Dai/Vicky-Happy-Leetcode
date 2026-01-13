# T
# dp[l][r][m] = 把区间 stones[l..r] 合成 m 堆所需要的最小代价

class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        """
        本题使用 Interval DP + 3D 状态表示：
        dp[l][r][m] = 把 stones[l..r] 合成 m 堆的最小代价（m ∈ 1..k）
        
        最终答案 = dp[0][n-1][1]
        """

        n = len(stones)

        # 如果不能最终合成 1 堆，直接返回 -1
        # 每次操作能让堆数减少 (k-1)，所以 (n - 1) 必须是 (k - 1) 的倍数
        if (n - 1) % (k - 1) != 0:
            return -1

        # 前缀和，方便计算任意区间 stones[l..r] 的和
        prefix = [0]
        for x in stones:
            prefix.append(prefix[-1] + x)

        def range_sum(l, r):
            return prefix[r + 1] - prefix[l]

        INF = float('inf')

        # dp[l][r][m]:
        #    将 stones[l..r] 合并成 m 堆的最小代价（1 ≤ m ≤ k）
        dp = [[[INF] * (k + 1) for _ in range(n)] for __ in range(n)]

        # 区间长度为 1 的情况：只能形成 1 堆，代价是 0
        for i in range(n):
            dp[i][i][1] = 0

        # 按区间长度进行 Interval DP（标准写法）
        for length in range(2, n + 1):                     # 区间长度从 2 到 n
            for l in range(0, n - length + 1):             # 左端点 l
                r = l + length - 1                         # 右端点 r

                # Case 1: 先让区间合成 m 堆（2..k）
                # 合成 m 堆的方式：
                #   左边形成 1 堆，右边形成 m-1 堆
                #   然后拼在一起，就自然是 m 堆
                for m in range(2, k + 1):                  # m = 2..k
                    # 分割点 p 每次跳 k-1：因为每次合并 k 堆减少 (k-1) 堆
                    # 这是石子合并类 DP 的优化技巧（也是题目性质决定的）
                    for p in range(l, r, k - 1):
                        dp[l][r][m] = min(
                            dp[l][r][m],
                            dp[l][p][1] + dp[p + 1][r][m - 1]
                        )

                # Case 2: 如果区间可以最终合成 1 堆
                # 条件：(length - 1) % (k - 1) == 0
                # 因为 length 堆最终想变成 1 堆，必须能通过多次减少 (k-1) 堆实现
                if (length - 1) % (k - 1) == 0:
                    # 要形成 1 堆，必须先变成 k 堆 → 再执行一次 k→1
                    # dp[l][r][k]：区间先合成 k 堆的最小代价
                    # range_sum(l,r)：把这 k 堆合成 1 堆的代价（总和）
                    dp[l][r][1] = dp[l][r][k] + range_sum(l, r)

        # 整段 stones[0..n-1] 合成 1 堆的最小代价
        return dp[0][n - 1][1]

""" 每次只能把 k 堆变成 1 堆，所以区间不能一步到位，必须经历“变成 k 堆 → 再变成 1 堆”的过程。

因此我们让 dp[l][r][m] 记录“把区间 l..r 合成 m 堆的最小代价”。

区间由子区间合并得到：左边先合成 1 堆，右边合成 m-1 堆，就能组成 m 堆；如果要合成 1 堆，就必须先合成 k 堆再加一次总和。 """