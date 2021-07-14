"""
977. 有序数组的平方
数组 双指针 排序
简单


给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。

 

示例 1：

输入：nums = [-4,-1,0,3,10]
输出：[0,1,9,16,100]
解释：平方后，数组变为 [16,1,0,9,100]
排序后，数组变为 [0,1,9,16,100]
示例 2：

输入：nums = [-7,-3,2,3,11]
输出：[4,9,9,49,121]
 

提示：

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 已按 非递减顺序 排序
 

进阶：

请你设计时间复杂度为 O(n) 的算法解决本问题

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/squares-of-a-sorted-array
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        nums_len = len(nums)
        positive_index = 0
        while positive_index < nums_len - 1:
            if nums[positive_index] >= 0:
                break
            positive_index += 1
        negative_index = positive_index - 1 if positive_index >= 0 else 0
        sorted_list = []
        while not (negative_index < 0 and positive_index > nums_len - 1):
            positive_val = 10001 if positive_index > nums_len - 1 else nums[positive_index]
            negative_val = 10001 if negative_index < 0 else -nums[negative_index]
            if positive_val < negative_val:
                sorted_list.append(positive_val ** 2)
                positive_index += 1
            else:
                sorted_list.append(negative_val ** 2)
                negative_index -= 1
        return sorted_list


if __name__ == '__main__':
    solution = Solution()

    result = solution.sortedSquares([-4, -1, 0, 3, 10])
    print(result)
    assert result == [0, 1, 9, 16, 100]

    result = solution.sortedSquares([-7, -3, 2, 3, 11])
    print(result)
    assert result == [4, 9, 9, 49, 121]

    result = solution.sortedSquares([-5, -3, -2, -1])
    print(result)
    assert result == [1, 4, 9, 25]
