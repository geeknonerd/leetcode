"""
713. 乘积小于K的子数组
数组 滑动窗口
中等


给定一个正整数数组 nums和整数 k 。

请找出该数组内乘积小于 k 的连续的子数组的个数。

 

示例 1:

输入: nums = [10,5,2,6], k = 100
输出: 8
解释: 8个乘积小于100的子数组分别为: [10], [5], [2], [6], [10,5], [5,2], [2,6], [5,2,6]。
需要注意的是 [10,5,2] 并不是乘积小于100的子数组。
示例 2:

输入: nums = [1,2,3], k = 0
输出: 0
 

提示: 

1 <= nums.length <= 3 * 104
1 <= nums[i] <= 1000
0 <= k <= 106

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-product-less-than-k
"""
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        prod = 1
        ans = 0
        left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k and left <= right:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100)
    print(result)
    assert result == 8

    result = solution.numSubarrayProductLessThanK([1, 2, 3], 0)
    print(result)
    assert result == 0
