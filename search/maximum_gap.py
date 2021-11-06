"""
164. 最大间距
数组 桶排序 基数排序 排序


给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。

示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-gap
"""
import math
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        size = 0
        min_val = math.inf
        max_val = -1
        for i in nums:
            size += 1
            min_val = min(min_val, i)
            max_val = max(max_val, i)
        if size < 2:
            return 0
        d = max(1, (max_val - min_val) // (size - 1))
        bucket_size = (max_val - min_val) // d + 1
        bucket = [[math.inf, -1] for _ in range(bucket_size)]
        for i in range(size):
            idx = (nums[i] - min_val) // d
            bucket[idx][0] = min(bucket[idx][0], nums[i])
            bucket[idx][1] = max(bucket[idx][1], nums[i])
        ret = 0
        prev = 0
        for i in range(1, bucket_size):
            if bucket[i][0] == math.inf:
                continue
            ret = max(ret, bucket[i][0] - bucket[prev][1])
            prev = i
        return ret


if __name__ == '__main__':
    solution = Solution()

    result = solution.maximumGap([3, 6, 9, 1])
    print(result)
    assert result == 3

    result = solution.maximumGap([10])
    print(result)
    assert result == 0
