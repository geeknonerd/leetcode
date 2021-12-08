"""
152. 乘积最大子数组
数组 动态规划
中等


给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 

示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        size = len(nums)
        max_f = nums.copy()
        min_f = nums.copy()
        for i in range(1, size):
            max_f[i] = max(max_f[i - 1] * nums[i], nums[i], min_f[i - 1] * nums[i])
            min_f[i] = min(min_f[i - 1] * nums[i], nums[i], max_f[i - 1] * nums[i])
        ans = max_f[0]
        for i in range(1, size):
            ans = max(ans, max_f[i])
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.maxProduct([2, 3, -2, 4])
    print(result)
    assert result == 6

    result = solution.maxProduct([-2, 0, -1])
    print(result)
    assert result == 0

    result = solution.maxProduct([-3, -1, -1])
    print(result)
    assert result == 3
