"""
53. 最大子序和
数组 分治 动态规划
简单


给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [0]
输出：0
示例 4：

输入：nums = [-1]
输出：-1
示例 5：

输入：nums = [-100000]
输出：-100000
 

提示：

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
 

进阶：如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的 分治法 求解。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre, max_num = 0, nums[0]
        for i in nums:
            pre = max(pre + i, i)
            max_num = max(pre, max_num)
        return max_num


if __name__ == '__main__':
    solution = Solution()

    result = solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(result)
    assert result == 6

    result = solution.maxSubArray([1])
    print(result)
    assert result == 1

    result = solution.maxSubArray([0])
    print(result)
    assert result == 0

    result = solution.maxSubArray([-1])
    print(result)
    assert result == -1

    result = solution.maxSubArray([-100000])
    print(result)
    assert result == -100000
