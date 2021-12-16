"""
931. 下降路径最小和
数组 动态规划 矩阵
中等


给你一个 n x n 的 方形 整数数组 matrix ，请你找出并返回通过 matrix 的下降路径 的 最小和 。

下降路径 可以从第一行中的任何元素开始，并从每一行中选择一个元素。在下一行选择的元素和当前行所选元素最多相隔一列（即位于正下方或者沿对角线向左或者向右的第一个元素）。具体来说，位置 (row, col) 的下一个元素应当是 (row + 1, col - 1)、(row + 1, col) 或者 (row + 1, col + 1) 。

 

示例 1：

输入：matrix = [[2,1,3],[6,5,4],[7,8,9]]
输出：13
解释：下面是两条和最小的下降路径，用加粗+斜体标注：
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
示例 2：

输入：matrix = [[-19,57],[-40,-5]]
输出：-59
解释：下面是一条和最小的下降路径，用加粗+斜体标注：
[[-19,57],
 [-40,-5]]
示例 3：

输入：matrix = [[-48]]
输出：-48
 

提示：

n == matrix.length
n == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-falling-path-sum
"""
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        while len(matrix) >= 2:
            row = matrix.pop()
            size = len(row)
            for i in range(size):
                matrix[-1][i] += min(row[max(0, i-1):min(size, i+2)])
        return min(matrix[0])


if __name__ == '__main__':
    solution = Solution()

    result = solution.minFallingPathSum([[2, 1, 3], [6, 5, 4], [7, 8, 9]])
    print(result)
    assert result == 13

    result = solution.minFallingPathSum([[-19, 57], [-40, -5]])
    print(result)
    assert result == -59

    result = solution.minFallingPathSum([[-48]])
    print(result)
    assert result == -48
