"""
63. 不同路径 II
数组 动态规划 矩阵
中等


一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

 

示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1
 

提示：

m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] 为 0 或 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
"""
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        r_size, c_size = len(obstacleGrid), len(obstacleGrid[0])
        res = [0] * c_size

        res[0] = 1 if obstacleGrid[0][0] == 0 else 0
        for i in range(r_size):
            for j in range(c_size):
                if obstacleGrid[i][j] == 1:
                    res[j] = 0
                    continue
                if j - 1 >= 0 and obstacleGrid[i][j-1] == 0:
                    res[j] += res[j-1]
        return res[c_size-1]


if __name__ == '__main__':
    solution = Solution()

    result = solution.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
    print(result)
    assert result == 2

    result = solution.uniquePathsWithObstacles([[0, 1], [0, 0]])
    print(result)
    assert result == 1
