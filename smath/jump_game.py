"""
55. 跳跃游戏
贪心 数组 动态规划
中等


给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

 

示例 1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。
示例 2：

输入：nums = [3,2,1,0,4]
输出：false
解释：无论怎样，总会到达下标为 3 的位置。但该下标的最大跳跃长度是 0 ， 所以永远不可能到达最后一个下标。
 

提示：

1 <= nums.length <= 3 * 104
0 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n, max_pos = len(nums), 0
        for i in range(n):
            if i <= max_pos:
                max_pos = max(max_pos, i + nums[i])
                if max_pos >= n - 1:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()

    result = solution.canJump([2, 3, 1, 1, 4])
    print(result)
    assert result is True

    result = solution.canJump([3, 2, 1, 0, 4])
    print(result)
    assert result is False
