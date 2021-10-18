"""
75. 颜色分类
数组 双指针 排序
中等


给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

 

示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]
示例 2：

输入：nums = [2,0,1]
输出：[0,1,2]
示例 3：

输入：nums = [0]
输出：[0]
示例 4：

输入：nums = [1]
输出：[1]
 

提示：

n == nums.length
1 <= n <= 300
nums[i] 为 0、1 或 2
 

进阶：

你可以不使用代码库中的排序函数来解决这道题吗？
你能想出一个仅使用常数空间的一趟扫描算法吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
"""
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if size < 2:
            return
        left, right = 0, size - 1
        i = 0
        while i <= right:
            while i <= right and nums[i] == 2:
                nums[i], nums[right] = nums[right], nums[i]
                right -= 1
            if nums[i] == 0:
                nums[left], nums[i] = nums[i], nums[left]
                left += 1
            i += 1


if __name__ == '__main__':
    solution = Solution()

    result = [2, 0, 2, 1, 1, 0]
    solution.sortColors(result)
    print(result)
    assert result == [0, 0, 1, 1, 2, 2]

    result = [2,0,1]
    solution.sortColors(result)
    print(result)
    assert result == [0,1,2]

    result = [0]
    solution.sortColors(result)
    print(result)
    assert result == [0]

    result = [1]
    solution.sortColors(result)
    print(result)
    assert result == [1]
