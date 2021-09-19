"""
217. 存在重复元素
数组 哈希表 排序
简单


给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/contains-duplicate
"""
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        exists = set()
        for i in nums:
            if i in exists:
                return True
            exists.add(i)
        return False


if __name__ == '__main__':
    solution = Solution()

    result = solution.containsDuplicate([1, 2, 3, 1])
    print(result)
    assert result is True

    result = solution.containsDuplicate([1, 2, 3, 4])
    print(result)
    assert result is False

    result = solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
    print(result)
    assert result is True
