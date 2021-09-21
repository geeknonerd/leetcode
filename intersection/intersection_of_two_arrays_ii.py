"""
350. 两个数组的交集 II
数组 哈希表 双指针 二分查找 排序
简单


给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/intersection-of-two-arrays-ii
"""
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        size1, size2 = len(nums1), len(nums2)
        p1, p2 = 0, 0
        ans = []
        while p1 < size1 and p2 < size2:
            if nums1[p1] == nums2[p2]:
                ans.append(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.intersect([1, 2, 2, 1], [2, 2])
    print(result)
    assert set(result) == set([2, 2])

    result = solution.intersect([4, 9, 5], nums2=[9, 4, 9, 8, 4])
    print(result)
    assert set(result) == set([4, 9])
