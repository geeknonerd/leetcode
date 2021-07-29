"""
994. 腐烂的橘子
广度优先搜索 数组 矩阵
中等


在给定的网格中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，任何与腐烂的橘子（在 4 个正方向上）相邻的新鲜橘子都会腐烂。

返回直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1。

 

示例 1：



输入：[[2,1,1],[1,1,0],[0,1,1]]
输出：4
示例 2：

输入：[[2,1,1],[0,1,1],[1,0,1]]
输出：-1
解释：左下角的橘子（第 2 行， 第 0 列）永远不会腐烂，因为腐烂只会发生在 4 个正向上。
示例 3：

输入：[[0,2]]
输出：0
解释：因为 0 分钟时已经没有新鲜橘子了，所以答案就是 0 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotting-oranges
"""
from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row_len, col_len = len(grid), len(grid[0])
        remains = set()
        queue = deque()
        bad = set()
        for i in range(row_len):
            for j in range(col_len):
                if grid[i][j] == 1:
                    remains.add((i, j))
                elif grid[i][j] == 2:
                    queue.append((i, j))
                    bad.add((i, j))
        if not remains:
            return 0
        n = -1
        while queue:
            n += 1
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for ni, nj in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                    if 0 <= ni < row_len and 0 <= nj < col_len and (ni, nj) in remains and (ni, nj) not in bad:
                        queue.append((ni, nj))
                        remains.remove((ni, nj))
                        bad.add((ni, nj))
        if remains:
            return -1
        return n


if __name__ == '__main__':
    solution = Solution()

    result = solution.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    print(result)
    assert result == 4

    result = solution.orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]])
    print(result)
    assert result == -1

    result = solution.orangesRotting([[0, 2]])
    print(result)
    assert result == 0

    result = solution.orangesRotting([[0]])
    print(result)
    assert result == 0

    result = solution.orangesRotting([[1]])
    print(result)
    assert result == -1
