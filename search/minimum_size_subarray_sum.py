"""
209. 长度最小的子数组
数组 二分查找 前缀和 滑动窗口
中等


给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其和 ≥ target 的长度最小的 连续子数组 [numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

 

示例 1：

输入：target = 7, nums = [2,3,1,2,4,3]
输出：2
解释：子数组 [4,3] 是该条件下的长度最小的子数组。
示例 2：

输入：target = 4, nums = [1,4,4]
输出：1
示例 3：

输入：target = 11, nums = [1,1,1,1,1,1,1,1]
输出：0
 

提示：

1 <= target <= 10^9
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
"""
from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        ans = n + 1
        total = 0
        start, end = 0, 0
        while end < n:
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
            end += 1
        return 0 if ans == n + 1 else ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3])
    print(result)
    assert result == 2

    result = solution.minSubArrayLen(4, [1, 4, 4])
    print(result)
    assert result == 1

    result = solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1])
    print(result)
    assert result == 0
