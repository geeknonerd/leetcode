"""
485. 最大连续 1 的个数
数组
简单


给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。

 

示例 1：

输入：nums = [1,1,0,1,1,1]
输出：3
解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
示例 2:

输入：nums = [1,0,1,1,0,1]
输出：2
 

提示：

1 <= nums.length <= 10^5
nums[i] 不是 0 就是 1.

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/max-consecutive-ones
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_cnt = 0
        max_cnt = 0
        for i in nums:
            if i == 1:
                cur_cnt += 1
            else:
                max_cnt = max(max_cnt, cur_cnt)
                cur_cnt = 0
        max_cnt = max(max_cnt, cur_cnt)
        return max_cnt


if __name__ == '__main__':
    solution = Solution()

    result = solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1])
    print(result)
    assert result == 3

    result = solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1])
    print(result)
    assert result == 2
