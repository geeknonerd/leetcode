"""
59. 螺旋矩阵 II
数组 矩阵 模拟
中等


给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：

1 <= n <= 20

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix-ii
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        changes = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        matrix = [[0] * n for _ in range(n)]
        row, col, index = 0, 0, 0
        for i in range(n * n):
            matrix[row][col] = i + 1
            r, c = row + changes[index][0], col + changes[index][1]
            if r < 0 or r >= n or c < 0 or c >= n or matrix[r][c] > 0:
                index = (index + 1) % 4
            row, col = row + changes[index][0], col + changes[index][1]
        return matrix


if __name__ == '__main__':
    solution = Solution()

    result = solution.generateMatrix(3)
    print(result)
    assert result == [[1, 2, 3], [8, 9, 4], [7, 6, 5]]

    result = solution.generateMatrix(1)
    print(result)
    assert result == [[1]]
