"""
215. 数组中的第K个最大元素
数组 分治 快速选择 排序 堆（优先队列）
中等


给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

 

示例 1:

输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
 

提示：

1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/kth-largest-element-in-an-array
"""
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(n_list: List[int], left: int, right: int) -> int:
            x: int = n_list[right]
            i, j = left - 1, left
            while j < right:
                if n_list[j] <= x:
                    i += 1
                    n_list[i], n_list[j] = n_list[j], n_list[i]
                j += 1
            n_list[i + 1], n_list[right] = n_list[right], n_list[i + 1]
            return i + 1

        def quick_select(n_list: List[int], left: int, right: int, i: int):
            q: int = partition(n_list, left, right)
            if q == i:
                return n_list[q]
            else:
                return quick_select(n_list, q + 1, right, i) if q < i else quick_select(n_list, left, q - 1, i)

        return quick_select(nums, 0, len(nums) - 1, len(nums) - k)


if __name__ == '__main__':
    solution = Solution()

    result = solution.findKthLargest([3, 2, 1, 5, 6, 4], 2)
    print(result)
    assert result == 5

    result = solution.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    print(result)
    assert result == 4
