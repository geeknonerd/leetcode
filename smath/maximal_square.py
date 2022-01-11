"""
221. 最大正方形
数组 动态规划 矩阵
中等


在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。

 

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：4
示例 2：


输入：matrix = [["0","1"],["1","0"]]
输出：1
示例 3：

输入：matrix = [["0"]]
输出：0
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] 为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-square
"""
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r_size, c_size = len(matrix), len(matrix[0])
        if r_size == 0 or c_size == 0:
            return 0
        max_side = 0
        dp = [[0] * c_size for _ in range(r_size)]
        for i in range(r_size):
            for j in range(c_size):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side


if __name__ == '__main__':
    solution = Solution()

    result = solution.maximalSquare(
        [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]])
    print(result)
    assert result == 4

    result = solution.maximalSquare([["0", "1"], ["1", "0"]])
    print(result)
    assert result == 1

    result = solution.maximalSquare([["0"]])
    print(result)
    assert result == 0
