"""
198. 打家劫舍
数组 动态规划
中等


你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

1 <= nums.length <= 100
0 <= nums[i] <= 400

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
"""
from typing import List


class Solution:

    def __init__(self):
        self.nums = []
        self.memory_cache = {}

    def rob(self, nums: List[int]) -> int:
        self.memory_cache = {}
        if not nums:
            return 0
        self.nums = nums
        size = len(self.nums)
        return self.max_sum(size-1)

    def max_sum(self, n):
        if n == 0:
            return self.nums[0]
        elif n == 1:
            return max(self.nums[0], self.nums[1])
        if n in self.memory_cache:
            return self.memory_cache[n]
        ans = max(self.max_sum(n - 2) + self.nums[n], self.max_sum(n - 1))
        self.memory_cache[n] = ans
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.rob([1, 2, 3, 1])
    print(result)
    assert result == 4

    result = solution.rob([2, 7, 9, 3, 1])
    print(result)
    assert result == 12
