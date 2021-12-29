"""
1567. 乘积为正数的最长子数组长度
贪心 数组 动态规划
中等


给你一个整数数组 nums ，请你求出乘积为正数的最长子数组的长度。

一个数组的子数组是由原数组中零个或者更多个连续数字组成的数组。

请你返回乘积为正数的最长子数组长度。

 

示例  1：

输入：nums = [1,-2,-3,4]
输出：4
解释：数组本身乘积就是正数，值为 24 。
示例 2：

输入：nums = [0,1,-2,-3,-4]
输出：3
解释：最长乘积为正数的子数组为 [1,-2,-3] ，乘积为 6 。
注意，我们不能把 0 也包括到子数组中，因为这样乘积为 0 ，不是正数。
示例 3：

输入：nums = [-1,-2,-3,0,1]
输出：2
解释：乘积为正数的最长子数组是 [-1,-2] 或者 [-2,-3] 。
示例 4：

输入：nums = [-1,2]
输出：1
示例 5：

输入：nums = [1,2,3,5,-6,4,0,10]
输出：4
 

提示：

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-subarray-with-positive-product
"""
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        size = len(nums)
        positive, negative = [0] * size, [0] * size
        if nums[0] > 0:
            positive[0] = 1
        elif nums[0] < 0:
            negative[0] = 1
        max_size = positive[0]
        for i in range(1, size):
            if nums[i] > 0:
                positive[i] = positive[i - 1] + 1
                negative[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
            elif nums[i] < 0:
                positive[i] = (negative[i - 1] + 1 if negative[i - 1] > 0 else 0)
                negative[i] = positive[i - 1] + 1
            else:
                positive[i] = negative[i] = 0
            max_size = max(max_size, positive[i])
        return max_size


if __name__ == '__main__':
    solution = Solution()

    result = solution.getMaxLen([1, -2, -3, 4])
    print(result)
    assert result == 4

    result = solution.getMaxLen([0, 1, -2, -3, -4])
    print(result)
    assert result == 3

    result = solution.getMaxLen([-1, -2, -3, 0, 1])
    print(result)
    assert result == 2

    result = solution.getMaxLen([-1, 2])
    print(result)
    assert result == 1

    result = solution.getMaxLen([1, 2, 3, 5, -6, 4, 0, 10])
    print(result)
    assert result == 4
