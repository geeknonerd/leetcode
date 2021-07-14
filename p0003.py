"""
35. 搜索插入位置
数组 二分查找
简单


给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

示例 1:

输入: [1,3,5,6], 5
输出: 2
示例 2:

输入: [1,3,5,6], 2
输出: 1
示例 3:

输入: [1,3,5,6], 7
输出: 4
示例 4:

输入: [1,3,5,6], 0
输出: 0

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-insert-position
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target, 0, len(nums)-1)

    def binary_search(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left >= right:
            if target <= nums[left]:
                return left
            else:
                return left + 1
        middle = (left + right) // 2
        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            return self.binary_search(nums, target, left, middle - 1)
        else:
            return self.binary_search(nums, target, middle + 1, right)


if __name__ == '__main__':
    solution = Solution()

    result = solution.searchInsert([1, 3, 5, 6], 5)
    print(result)
    assert result == 2

    result = solution.searchInsert([1, 3, 5, 6], 2)
    print(result)
    assert result == 1

    result = solution.searchInsert([1, 3, 5, 6], 7)
    print(result)
    assert result == 4

    result = solution.searchInsert([1, 3, 5, 6], 0)
    print(result)
    assert result == 0
