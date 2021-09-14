"""
673. 最长递增子序列的个数
树状数组 线段树 数组 动态规划
中等


给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence
"""
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 1
        dp = [1] * n
        cnt = [1] * n
        max_len = 0
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        cnt[i] = cnt[j]
                    elif dp[j] + 1 == dp[i]:
                        cnt[i] += cnt[j]
            max_len = max(max_len, dp[i])
        res = 0
        for i in range(n):
            if dp[i] == max_len:
                res += cnt[i]
        return res


if __name__ == '__main__':
    solution = Solution()

    result = solution.findNumberOfLIS([1, 3, 5, 4, 7])
    print(result)
    assert result == 2

    result = solution.findNumberOfLIS([2, 2, 2, 2, 2])
    print(result)
    assert result == 5
