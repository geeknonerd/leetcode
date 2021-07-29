"""
542. 01 矩阵
广度优先搜索 数组 动态规划
中等


给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

 

示例 1：



输入：mat = [[0,0,0],[0,1,0],[0,0,0]]
输出：[[0,0,0],[0,1,0],[0,0,0]]
示例 2：



输入：mat = [[0,0,0],[0,1,0],[1,1,1]]
输出：[[0,0,0],[0,1,0],[1,2,1]]
 

提示：

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
mat[i][j] is either 0 or 1.
mat 中至少有一个 0 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/01-matrix
"""
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dest = [[0]*n for _ in range(m)]
        zeros = []
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    zeros.append((i, j))
        seen = set(zeros)
        queue = zeros[:]
        while queue:
            i, j = queue.pop(0)
            for ni, nj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= ni < m and 0 <= nj < n and (ni, nj) not in seen:
                    dest[ni][nj] = dest[i][j] + 1
                    queue.append((ni, nj))
                    seen.add((ni, nj))
        return dest


if __name__ == '__main__':
    solution = Solution()

    result = solution.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print(result)
    assert result == [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

    result = solution.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
    print(result)
    assert result == [[0, 0, 0], [0, 1, 0], [1, 2, 1]]
