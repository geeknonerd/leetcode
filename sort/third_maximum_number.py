"""
414. 第三大的数
数组 排序
简单


给你一个非空数组，返回此数组中 第三大的数 。如果不存在，则返回数组中最大的数。

 

示例 1：

输入：[3, 2, 1]
输出：1
解释：第三大的数是 1 。
示例 2：

输入：[1, 2]
输出：2
解释：第三大的数不存在, 所以返回最大的数 2 。
示例 3：

输入：[2, 2, 3, 1]
输出：1
解释：注意，要求返回第三大的数，是指在所有不同数字中排第三大的数。
此例中存在两个值为 2 的数，它们都排第二。在所有不同数字中排第三大的数为 1 。
 

提示：

1 <= nums.length <= 10^4
-2^31 <= nums[i] <= 2^31 - 1
 

进阶：你能设计一个时间复杂度 O(n) 的解决方案吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/third-maximum-number
"""
import math
from typing import List
from collections import deque


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sorted_nums = deque([-math.inf]*3)
        tmp_set = set()
        for i in nums:
            tmp_set.add(i)
            for _ in range(3):
                tmp_set.add(sorted_nums.popleft())
                max_num = max(tmp_set)
                tmp_set.remove(max_num)
                sorted_nums.append(max_num)
        return sorted_nums[0] if sorted_nums[-1] == -math.inf else sorted_nums[-1]


if __name__ == '__main__':
    solution = Solution()

    result = solution.thirdMax([3, 2, 1])
    print(result)
    assert result == 1

    result = solution.thirdMax([1, 2])
    print(result)
    assert result == 2

    result = solution.thirdMax([2, 2, 3, 1])
    print(result)
    assert result == 1
