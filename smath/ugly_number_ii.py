"""
264. 丑数 II
哈希表 数学 动态规划 堆（优先队列）
中等


给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是只包含质因数 2、3 和/或 5 的正整数。

 

示例 1：

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。
示例 2：

输入：n = 1
输出：1
解释：1 通常被视为丑数。
 

提示：

1 <= n <= 1690

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number-ii
"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        p2 = p3 = p5 = 1
        for i in range(2, n+1):
            n2, n3, n5 = dp[p2] * 2, dp[p3] * 3, dp[p5]*5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                p2 += 1
            if dp[i] == n3:
                p3 += 1
            if dp[i] == n5:
                p5 += 1
        return dp[n]


if __name__ == '__main__':
    solution = Solution()

    result = solution.nthUglyNumber(10)
    print(result)
    assert result == 12

    result = solution.nthUglyNumber(1)
    print(result)
    assert result == 1

