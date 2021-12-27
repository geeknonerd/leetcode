"""
1137. 第 N 个泰波那契数
记忆化搜索 数学 动态规划
简单


泰波那契序列 Tn 定义如下： 

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

 

示例 1：

输入：n = 4
输出：4
解释：
T_3 = 0 + 1 + 1 = 2
T_4 = 1 + 1 + 2 = 4
示例 2：

输入：n = 25
输出：1389537
 

提示：

0 <= n <= 37
答案保证是一个 32 位整数，即 answer <= 2^31 - 1。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-th-tribonacci-number
"""


class Solution:
    cached = {}

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n < 3:
            return 1
        if n in self.cached:
            return self.cached.get(n)
        res = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        self.cached[n] = res
        return res


if __name__ == '__main__':
    solution = Solution()

    result = solution.tribonacci(4)
    print(result)
    assert result == 4

    result = solution.tribonacci(25)
    print(result)
    assert result == 1389537
