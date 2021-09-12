"""
413. 等差数列划分
数组 动态规划
中等


如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

 

示例 1：

输入：nums = [1,2,3,4]
输出：3
解释：nums 中有三个子等差数组：[1, 2, 3]、[2, 3, 4] 和 [1,2,3,4] 自身。
示例 2：

输入：nums = [1]
输出：0
 

提示：

1 <= nums.length <= 5000
-1000 <= nums[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/arithmetic-slices
"""
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0]*n
        for i in range(1, n-1):
            if nums[i-1] + nums[i+1] == nums[i]*2:
                dp[i] = dp[i-1]+1
        return sum(dp)


if __name__ == '__main__':
    solution = Solution()

    result = solution.numberOfArithmeticSlices([1, 2, 3, 4])
    print(result)
    assert result == 3

    result = solution.numberOfArithmeticSlices([1])
    print(result)
    assert result == 0
