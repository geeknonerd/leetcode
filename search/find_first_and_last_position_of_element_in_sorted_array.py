"""
34. 在排序数组中查找元素的第一个和最后一个位置
数组 二分查找
中等


给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？
 

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例 2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]
 

提示：

0 <= nums.length <= 105
-10^9 <= nums[i] <= 10^9
nums 是一个非递减数组
-10^9 <= target <= 10^9

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False) - 1
        if left <= right < len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        return [-1, -1]

    def binary_search(self, nums: List[int], target: int, is_lower: bool) -> int:
        left = 0
        right = len(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (is_lower and nums[mid] >= target):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.searchRange([5, 7, 7, 8, 8, 10], 8)
    print(result)
    assert result == [3, 4]

    result = solution.searchRange([5, 7, 7, 8, 8, 10], 6)
    print(result)
    assert result == [-1, -1]

    result = solution.searchRange([], 0)
    print(result)
    assert result == [-1, -1]
