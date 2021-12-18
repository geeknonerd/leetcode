"""
64. 最小路径和
数组 动态规划 矩阵
中等


给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

 

示例 1：


输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
示例 2：

输入：grid = [[1,2,3],[4,5,6]]
输出：12
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 100


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-path-sum
"""
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1, rows):
            for j in range(1, cols):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        return dp[rows-1][cols-1]


if __name__ == '__main__':
    solution = Solution()

    result = solution.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]])
    print(result)
    assert result == 7

    result = solution.minPathSum([[1, 2, 3], [4, 5, 6]])
    print(result)
    assert result == 12
