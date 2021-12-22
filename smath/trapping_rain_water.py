"""
42. 接雨水
栈 数组 双指针 动态规划 单调栈
困难


给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
1 <= n <= 2 * 10^4
0 <= height[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trapping-rain-water
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        size = len(height)
        left_max = [0] * size
        left_max[0] = height[0]
        for i in range(1, size):
            left_max[i] = max(left_max[i - 1], height[i])

        right_max = [0] * size
        right_max[-1] = height[-1]
        for i in range(size - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])

        return sum(min(left_max[i], right_max[i]) - height[i] for i in range(size))


if __name__ == '__main__':
    solution = Solution()

    result = solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(result)
    assert result == 6

    result = solution.trap([4, 2, 0, 3, 2, 5])
    print(result)
    assert result == 9
