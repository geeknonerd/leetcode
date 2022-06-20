"""
349. 两个数组的交集
数组 哈希表 双指针 二分查找 排序
简单


给定两个数组 nums1 和 nums2 ，返回 它们的交集 。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
解释：[4,9] 也是可通过的
 

提示：

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/intersection-of-two-arrays
"""
from typing import List


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        intersection = []
        s_len1 = len(nums1)
        s_len2 = len(nums2)
        s_i1, s_i2 = 0, 0
        while s_i1 < s_len1 and s_i2 < s_len2:
            n1 = nums1[s_i1]
            n2 = nums2[s_i2]
            if n1 == n2:
                if not intersection or n1 != intersection[-1]:
                    intersection.append(n1)
                s_i1 += 1
                s_i2 += 1
            elif n1 > n2:
                s_i2 += 1
            else:
                s_i1 += 1
        return intersection


if __name__ == '__main__':
    solution = Solution()

    result = solution.intersection([1, 2, 2, 1], [2, 2])
    print(result)
    assert sorted(result) == sorted([2])

    result = solution.intersection([4, 9, 5], [9, 4, 9, 8, 4])
    print(result)
    assert sorted(result) == sorted([9, 4])

    result = solution.intersection([1], [1, 1])
    print(result)
    assert sorted(result) == sorted([1])
