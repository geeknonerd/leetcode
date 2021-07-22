"""
189. 旋转数组
数组 数学 双指针
中等


给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

 

进阶：

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
 

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释:
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
 

提示：

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_len = len(nums)
        left_index = (num_len - k) % num_len
        right_index = (left_index - 1) % num_len
        # new nums
        new_nums = []
        while left_index != right_index:
            new_nums.append(nums[left_index])
            left_index = (left_index + 1) % num_len
        new_nums.append(nums[left_index])
        # replace
        for i in range(num_len):
            nums[i] = new_nums[i]


if __name__ == '__main__':
    solution = Solution()

    num_list = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(num_list, 3)
    print(num_list)
    assert num_list == [5, 6, 7, 1, 2, 3, 4]

    num_list = [-1, -100, 3, 99]
    solution.rotate(num_list, 2)
    print(num_list)
    assert num_list == [3, 99, -1, -100]

    num_list = [1]
    solution.rotate(num_list, 1)
    print(num_list)
    assert num_list == [1]

    num_list = [1]
    solution.rotate(num_list, 0)
    print(num_list)
    assert num_list == [1]

    num_list = [1]
    solution.rotate(num_list, 2)
    print(num_list)
    assert num_list == [1]
