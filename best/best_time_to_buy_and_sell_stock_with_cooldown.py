"""
309. 最佳买卖股票时机含冷冻期
数组 动态规划
中等


给定一个整数数组，其中第 i 个元素代表了第 i 天的股票价格 。​

设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）:

你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。
卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。
示例:

输入: [1,2,3,0,2]
输出: 3
解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        f0, f1, f2 = -prices[0], 0, 0
        for i in range(1, n):
            new0 = max(f0, f2 - prices[i])
            new1 = f0 + prices[i]
            new2 = max(f1, f2)
            f0, f1, f2 = new0, new1, new2
        return max(f1, f2)


if __name__ == '__main__':
    solution = Solution()

    result = solution.maxProfit([1, 2, 3, 0, 2])
    print(result)
    assert result == 3
