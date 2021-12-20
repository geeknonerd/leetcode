"""
1314. 矩阵区域和
数组 矩阵 前缀和
中等


给你一个 m x n 的矩阵 mat 和一个整数 k ，请你返回一个矩阵 answer ，其中每个 answer[i][j] 是所有满足下述条件的元素 mat[r][c] 的和： 

i - k <= r <= i + k,
j - k <= c <= j + k 且
(r, c) 在矩阵内。
 

示例 1：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 1
输出：[[12,21,16],[27,45,33],[24,39,28]]
示例 2：

输入：mat = [[1,2,3],[4,5,6],[7,8,9]], k = 2
输出：[[45,45,45],[45,45,45],[45,45,45]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n, k <= 100
1 <= mat[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matrix-block-sum
"""
from typing import List


class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        mat_sum = [[0] * (n + 1) for _ in range(m + 1)]

        def get(x, y):
            x = max(min(x, m), 0)
            y = max(min(y, n), 0)
            return mat_sum[x][y]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                mat_sum[i][j] = mat_sum[i - 1][j] + mat_sum[i][j - 1] - mat_sum[i - 1][j - 1] + mat[i - 1][j - 1]

        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = get(i + k + 1, j + k + 1) - get(i - k, j + k + 1) - get(i + k + 1, j - k) + get(i - k,
                                                                                                            j - k)
        return res


if __name__ == '__main__':
    solution = Solution()

    result = solution.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1)
    print(result)
    assert result == [[12, 21, 16], [27, 45, 33], [24, 39, 28]]

    result = solution.matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2)
    print(result)
    assert result == [[45, 45, 45], [45, 45, 45], [45, 45, 45]]
