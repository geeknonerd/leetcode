"""
566. 重塑矩阵
数组 矩阵 模拟
简单


在 MATLAB 中，有一个非常有用的函数 reshape ，它可以将一个 m x n 矩阵重塑为另一个大小不同（r x c）的新矩阵，但保留其原始数据。

给你一个由二维数组 mat 表示的 m x n 矩阵，以及两个正整数 r 和 c ，分别表示想要的重构的矩阵的行数和列数。

重构后的矩阵需要将原始矩阵的所有元素以相同的 行遍历顺序 填充。

如果具有给定参数的 reshape 操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

 

示例 1：


输入：mat = [[1,2],[3,4]], r = 1, c = 4
输出：[[1,2,3,4]]
示例 2：


输入：mat = [[1,2],[3,4]], r = 2, c = 4
输出：[[1,2],[3,4]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 100
-1000 <= mat[i][j] <= 1000
1 <= r, c <= 300

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reshape-the-matrix
"""
from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m * n != r * c:
            return mat

        def next_num():
            for i in mat:
                for j in i:
                    yield j

        num_gen = next_num()
        new_mat = []
        for _ in range(r):
            rows = []
            for _ in range(c):
                rows.append(next(num_gen))
            new_mat.append(rows)
        return new_mat


if __name__ == '__main__':
    solution = Solution()

    result = solution.matrixReshape([[1, 2], [3, 4]], 1, 4)
    print(result)
    assert result == [[1, 2, 3, 4]]

    result = solution.matrixReshape([[1, 2], [3, 4]], 2, 4)
    print(result)
    assert result == [[1, 2], [3, 4]]
