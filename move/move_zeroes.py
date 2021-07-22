"""
283. 移动零
数组 双指针
简单


给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/move-zeroes
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left = 0
        while left < length and nums[left] != 0:
            left += 1
        right = left
        while left < length and right < length:
            if nums[right] == 0:
                right += 1
            else:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


if __name__ == '__main__':
    solution = Solution()

    num_list = [0, 1, 0, 3, 12]
    solution.moveZeroes(num_list)
    print(num_list)
    assert num_list == [1, 3, 12, 0, 0]

    num_list = [9, 6, 0, 1, 0, 0, 3, 2, 12]
    solution.moveZeroes(num_list)
    print(num_list)
    assert num_list == [9, 6, 1, 3, 2, 12, 0, 0, 0]

    num_list = [9, 6, 0, 1, 0, 0, 3, 2, 12, 0]
    solution.moveZeroes(num_list)
    print(num_list)
    assert num_list == [9, 6, 1, 3, 2, 12, 0, 0, 0, 0]

    num_list = [0]
    solution.moveZeroes(num_list)
    print(num_list)
    assert num_list == [0]

    num_list = [1]
    solution.moveZeroes(num_list)
    print(num_list)
    assert num_list == [1]

    num_list = []
    solution.moveZeroes(num_list)
    print(num_list)
    assert num_list == []
