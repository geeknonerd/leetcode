"""
200. 岛屿数量
深度优先搜索 广度优先搜索
中等


给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1
示例 2：

输入：grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
输出：3
 

提示：

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] 的值为 '0' 或 '1'

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-islands
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        nr = len(grid)
        if nr == 0:
            return 0
        nc = len(grid[0])

        def dfs(cr, cc):
            grid[cr][cc] = 0
            for x, y in (cr+1, cc), (cr-1, cc), (cr, cc+1), (cr, cc-1):
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == '1':
                    dfs(x, y)

        cnt = 0
        for r in range(nr):
            for c in range(nc):
                if grid[r][c] == '1':
                    cnt += 1
                    dfs(r, c)
        return cnt


if __name__ == '__main__':
    solution = Solution()

    _grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    result = solution.numIslands(_grid)
    print(result)
    assert result == 1

    _grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    result = solution.numIslands(_grid)
    print(result)
    assert result == 3
