"""
377. 组合总和 Ⅳ
数组 动态规划
中等


给你一个由 不同 整数组成的数组 nums ，和一个目标整数 target 。请你从 nums 中找出并返回总和为 target 的元素组合的个数。

题目数据保证答案符合 32 位整数范围。

 

示例 1：

输入：nums = [1,2,3], target = 4
输出：7
解释：
所有可能的组合为：
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
请注意，顺序不同的序列被视作不同的组合。
示例 2：

输入：nums = [9], target = 3
输出：0
 

提示：

1 <= nums.length <= 200
1 <= nums[i] <= 1000
nums 中的所有元素 互不相同
1 <= target <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum-iv
"""
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        pass


if __name__ == '__main__':
    solution = Solution()

    result = solution.combinationSum4([1, 2, 3], 4)
    print(result)
    assert result == 7

    result = solution.combinationSum4([9], 3)
    print(result)
    assert result == 0
