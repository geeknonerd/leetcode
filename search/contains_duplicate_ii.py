"""
219. 存在重复元素 II
数组 哈希表 滑动窗口
简单


给你一个整数数组 nums 和一个整数 k ，判断数组中是否存在两个 不同的索引 i 和 j ，满足 nums[i] == nums[j] 且 abs(i - j) <= k 。如果存在，返回 true ；否则，返回 false 。

 

示例 1：

输入：nums = [1,2,3,1], k = 3
输出：true
示例 2：

输入：nums = [1,0,1,1], k = 1
输出：true
示例 3：

输入：nums = [1,2,3,1,2,3], k = 2
输出：false
 

 

提示：

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/contains-duplicate-ii
"""
from collections import defaultdict
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_nears_dict = defaultdict(lambda: [-10**10, 10**10])
        for i in range(len(nums)):
            num_nears_dict[nums[i]][1] = min(i - num_nears_dict[nums[i]][0], num_nears_dict[nums[i]][1])
            num_nears_dict[nums[i]][0] = i
        for _, nk in num_nears_dict.values():
            if nk <= k:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()

    result = solution.containsNearbyDuplicate([1, 2, 3, 1], 3)
    print(result)
    assert result is True

    result = solution.containsNearbyDuplicate([1, 0, 1, 1], 1)
    print(result)
    assert result is True

    result = solution.containsNearbyDuplicate([1, 2, 3, 1, 2, 3], 2)
    print(result)
    assert result is False
