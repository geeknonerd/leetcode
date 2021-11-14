"""
560. 和为 K 的子数组
数组 哈希表 前缀和
中等


给你一个整数数组 nums 和一个整数 k ，请你统计并返回该数组中和为 k 的连续子数组的个数。

 

示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
 

提示：

1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
"""
from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, pre = 0, 0
        mp = defaultdict(lambda: 0)
        mp[0] = 1
        for i in nums:
            pre += i
            if pre - k in mp:
                count += mp[pre - k]
            mp[pre] += 1
        return count


if __name__ == '__main__':
    solution = Solution()

    result = solution.subarraySum([1, 1, 1], 2)
    print(result)
    assert result == 2

    result = solution.subarraySum([1, 2, 3], 3)
    print(result)
    assert result == 2
