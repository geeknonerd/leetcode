"""
322. 零钱兑换
广度优先搜索 数组 动态规划
中等


给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

 

示例 1：

输入：coins = [1, 2, 5], amount = 11
输出：3
解释：11 = 5 + 5 + 1
示例 2：

输入：coins = [2], amount = 3
输出：-1
示例 3：

输入：coins = [1], amount = 0
输出：0
示例 4：

输入：coins = [1], amount = 1
输出：1
示例 5：

输入：coins = [1], amount = 2
输出：2
 

提示：

1 <= coins.length <= 12
1 <= coins[i] <= 2^31 - 1
0 <= amount <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-change
"""
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cached = {}
        def dp(x) -> int:
            if cached.get(x) is not None:
                return cached.get(x)
            if x < 0:
                return -1
            if x == 0:
                return 0
            mini = float('Inf')
            for coin in coins:
                res = dp(x - coin)
                if 0 <= res < mini:
                    mini = res + 1
            dp_res = mini if mini < float('Inf') else -1
            cached[x] = dp_res
            return dp_res

        if amount < 1:
            return 0
        return dp(amount)


if __name__ == '__main__':
    solution = Solution()

    result = solution.coinChange([1, 2, 5], 11)
    print(result)
    assert result == 3

    result = solution.coinChange([2], 3)
    print(result)
    assert result == -1

    result = solution.coinChange([1], 0)
    print(result)
    assert result == 0

    result = solution.coinChange([1], 1)
    print(result)
    assert result == 1

    result = solution.coinChange([1], 2)
    print(result)
    assert result == 2
