"""
169. 多数元素
数组 哈希表 分治 计数 排序
简单


给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：[3,2,3]
输出：3
示例 2：

输入：[2,2,1,1,1,2,2]
输出：2
 

进阶：

尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/majority-element
"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        cnt = 0
        for n in nums:
            if cnt == 0:
                candidate = n
            cnt += 1 if candidate == n else -1
        return candidate


if __name__ == '__main__':
    solution = Solution()

    result = solution.majorityElement([3, 2, 3])
    print(result)
    assert result == 3

    result = solution.majorityElement([2, 2, 1, 1, 1, 2, 2])
    print(result)
    assert result == 2
